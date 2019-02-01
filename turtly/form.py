from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
import datetime
from .models import Entry, WorkoutBack, WorkoutArms, WorkoutChest, WorkoutLegs, Workout

class DateInput(forms.DateInput):
    input_type = 'date'

class StudyForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(StudyForm, self).__init__(*args, **kwargs)
        # assign a (computed, I assume) default value to the choice field
        self.initial['Study_Type_Entries'] = 'PRG'
        self.initial['link'] = 'None'
    class Meta:
        model = Entry
        fields = [
            "Study_Type_Entries",
            "topic",
            "content",
            "completed",
            "link",
            "date",
         ]
        labels = {
            'Study_Type_Entries': 'Type'
        }
        widgets = {
            'date': DateInput(),
            'content': forms.Textarea(attrs={'rows':10, 'cols':50}),
            }

class WorkoutBackForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(WorkoutBackForm, self).__init__(*args, **kwargs)
        # assign a (computed, I assume) default value to the choice field
        for field_name in self.fields:
            field = self.fields.get(field_name)
            if field and isinstance(field , forms.TypedChoiceField):
                field.choices = field.choices[1:]    
    class Meta:
        model = Workout
        fields = [
            "BACK_EX",
            "AMOUNT"
         ]
        labels = {
             'BACK_EX': ''
        }
        widgets = {
            'BACK_EX': forms.RadioSelect,
            }
class WorkoutArmsForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(WorkoutArmsForm, self).__init__(*args, **kwargs)
        # assign a (computed, I assume) default value to the choice field
        for field_name in self.fields:
            field = self.fields.get(field_name)
            if field and isinstance(field , forms.TypedChoiceField):
                field.choices = field.choices[1:]    
    class Meta:
        model = Workout
        fields = [
            "ARM_EX",
            "AMOUNT",
         ]
        labels = {
            'ARM_EX': ''
        }
        widgets = {
            'ARM_EX': forms.RadioSelect,
            }
class WorkoutLegsForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(WorkoutLegsForm, self).__init__(*args, **kwargs)
        # assign a (computed, I assume) default value to the choice field
        for field_name in self.fields:
            field = self.fields.get(field_name)
            if field and isinstance(field , forms.TypedChoiceField):
                field.choices = field.choices[1:]    
    class Meta:
        model = Workout
        fields = [
            "LEG_EX",
            "AMOUNT",
         ]
        labels = {
            'LEG_EX': ''
        }
        widgets = {
            'LEG_EX': forms.RadioSelect,
            }

class WorkoutChestForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(WorkoutChestForm, self).__init__(*args, **kwargs)
        # assign a (computed, I assume) default value to the choice field
        for field_name in self.fields:
            field = self.fields.get(field_name)
            if field and isinstance(field , forms.TypedChoiceField):
                field.choices = field.choices[1:]        
    class Meta:
        model = Workout
        fields = [
            "CHEST_EX",
            "AMOUNT",
         ]
        labels = {
            'CHEST_EX': ''
        }
        widgets = {
            'CHEST_EX': forms.RadioSelect,
            }
    