from django.shortcuts import render, redirect
from .calendar_code import Calendario
from .models import Entry, WorkoutBack, WorkoutArms, WorkoutChest, WorkoutLegs, Workout
from datetime import datetime, timedelta
from django.views.generic import ListView, CreateView, UpdateView, DetailView
from django.utils.safestring import mark_safe
from .form import StudyForm, WorkoutBackForm, WorkoutArmsForm, WorkoutChestForm, WorkoutLegsForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import calendar
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from itertools import groupby
from .workout_query import workout_get_dates, workout_to_post
from django.db.models import Count

# Create your views here.

class CalendarView(LoginRequiredMixin, ListView):
    model = Entry
    template_name = 'turtly/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        d = get_date(self.request.GET.get('month', None))
        cal = Calendario(str(self.request.user), d.year, d.month)
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)
        return context

def get_date(req_month):
    if req_month:
        year, month = (int(x) for x in req_month.split('-'))
        return datetime(year, month, day=1)
    return datetime.today()

def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month

def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month

@login_required

def studies(request):
    if request.method=='POST':
        form = StudyForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
    else:
        form = StudyForm()

    entry_list = Entry.objects.filter(user=request.user).order_by('-date')
    page = request.GET.get('page', 1)
    paginator = Paginator(entry_list, 8)

    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)

    context = {'studies': users, 'form': form}
    return render(request, 'turtly/studies.html', context)

class UpdateMe(LoginRequiredMixin, UpdateView):
    model= Entry
    fields= ['topic','content','completed']
    template_name='turtly/studies.html'
    success_url=reverse_lazy('turtly-home')
    def form_valid(self, form):
        form.instance.user= self.request.user
        return super().form_valid(form)

class DetailMe(LoginRequiredMixin, DetailView):
    model= Entry
    template_name='turtly/detail.html'

@login_required

def workout(request):
    
    if request.method=='POST' and 'BACK_EX' in request.POST:
        print(request.POST)
        WOBackForm = WorkoutBackForm(request.POST)
        WOChestForm = WorkoutChestForm()
        WOArmForm = WorkoutArmsForm()
        WOLegsForm = WorkoutLegsForm()
        if WOBackForm.is_valid():
            WOBackForm.instance.user = request.user
            WOBackForm.save()
            # messages.success(request, 'Exercise Submitted!')
            # return redirect('turtly-workout')
    elif request.method=='POST' and 'CHEST_EX' in request.POST:
        print(request.POST)
        WOBackForm = WorkoutBackForm()
        WOChestForm = WorkoutChestForm(request.POST)
        WOArmForm = WorkoutArmsForm()
        WOLegsForm = WorkoutLegsForm()        
        if WOChestForm.is_valid():
            WOChestForm.instance.user = request.user
            WOChestForm.save()
            # messages.success(request, 'Exercise Submitted!')
            # return redirect('turtly-workout')
    elif request.method=='POST' and 'ARM_EX' in request.POST:
        print(request.POST)
        WOBackForm = WorkoutBackForm()
        WOChestForm = WorkoutChestForm()
        WOArmForm = WorkoutArmsForm(request.POST)
        WOLegsForm = WorkoutLegsForm()       
        if WOArmForm.is_valid():
            WOArmForm.instance.user = request.user
            WOArmForm.save()
            # messages.success(request, 'Exercise Submitted!')
            # return redirect('turtly-workout')
    elif request.method=='POST' and 'LEG_EX' in request.POST:
        print(request.POST)
        WOBackForm = WorkoutBackForm()
        WOChestForm = WorkoutChestForm()
        WOArmForm = WorkoutArmsForm()
        WOLegsForm = WorkoutLegsForm(request.POST) 
        if WOLegsForm.is_valid():
            WOLegsForm.instance.user = request.user
            WOLegsForm.save()
            # messages.success(request, 'Exercise Submitted!')
            # return redirect('turtly-workout')

    else:
        WOBackForm = WorkoutBackForm()
        WOChestForm = WorkoutChestForm()
        WOArmForm = WorkoutArmsForm()
        WOLegsForm = WorkoutLegsForm()

    
    post = Workout.objects.extra(select={'day': 'date( date )'}).values('day').annotate(available=Count('date'))
    context = {'arms': WOArmForm, 'back': WOBackForm, 'chest': WOChestForm, 'legs': WOLegsForm, 'posts':workout_get_dates()}
    return render(request, 'turtly/workout.html', context)


def particular(request, days):
    list_ = []
    dict_ = {}
    dict_['date']= days
    list_.append(dict_)
    context = {'posts': workout_to_post(list_)}
    return render(request, 'turtly/workout-detail.html', context)

