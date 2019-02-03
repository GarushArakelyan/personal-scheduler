from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import datetime
from django.urls import reverse
from django.utils.safestring import mark_safe


# Create your models here.

class Entry(models.Model):

    STUDY_TYPE_ENTRIES = (
        ('PRG', 'Programming'),
        ('ADM', 'Admin'),
        ('DEV', 'DevOps'),
        ('LNG', 'Language'),
        ('OTH', 'Other'),
    )
    Study_Type_Entries = models.CharField(
        choices=STUDY_TYPE_ENTRIES,
        max_length=3,
        null=True,
        default=None,
    )
    user= models.ForeignKey(User,on_delete=models.CASCADE)
    topic= models.CharField(max_length=100)
    content= models.TextField()
    date= models.DateTimeField(default=timezone.now)
    completed= models.BooleanField(default=False)
    link= models.CharField(max_length=100)

    def __str__(self):
        return ('"{}", "{}", "{}"').format(self.Study_Type_Entries,self.topic,self.content)

    class Meta:
        verbose_name = "Entry"
        verbose_name_plural = "Entries"

    #get html url from calendar
    @property
    def get_html_url(self):
        url = reverse('post-detail', args=(self.id,))
        return f'<a href="{url}" > {self.topic}</a>'

    #Get html url from enty list
    @property
    def get_html_urls(self):
        url = reverse('post-update', args=(self.id,))
        return mark_safe(f'<a id="title_post" href="{url}"> {self.topic}</a>')
    @property
    def get_username(self):
        return self.user

class WorkoutBack(models.Model):
    user= models.ForeignKey(User,on_delete=models.CASCADE)
    date= models.DateTimeField(default=timezone.now)
    TYPE = (
        ('Trapezius Shrug', 'Trapezius Shrug'),
        ('Reverse Fly', 'Reverse Fly'),
        ('Dumbell Row', 'Dumbell Row'),
        ('Roman Chair', 'Roman Chair'),
    )
    BACK_EX = models.CharField(
        choices=TYPE,
        max_length = 30,
        null=True,
        default=None,
    )
    AMOUNT = models.CharField(max_length=70)
    def __str__(self):
        return ('"{}", "{}"').format(self.BACK_EX,self.AMOUNT)
    class Meta:
        verbose_name = "Workout Back"
        verbose_name_plural = "Workout Back"


class WorkoutChest(models.Model):
    user= models.ForeignKey(User,on_delete=models.CASCADE)
    date= models.DateTimeField(default=timezone.now)

    TYPE = (
        ('Bench Press', 'Bench Press'),
        ('Dumbell Press', 'Dumbell Press'),
        ('Fly', 'Fly'),
        ('Push Ups', 'Push Ups'),
    )
    CHEST_EX = models.CharField(
        choices=TYPE,
        max_length = 30,
        null=True,
        default=None,
    )
    AMOUNT = models.CharField(max_length=70)
    def __str__(self):
        return ('"{}", "{}"').format(self.CHEST_EX,self.AMOUNT)

    class Meta:
        verbose_name = "Workout Chest"
        verbose_name_plural = "Workout Chest"

class WorkoutArms(models.Model):
    user= models.ForeignKey(User,on_delete=models.CASCADE)
    date= models.DateTimeField(default=timezone.now)

    TYPE = (
        ('SHL_RS', 'Shoulder Raise'),
        ('Shoulder Press', 'Shoulder Press'),
        ('Overhead Triceps Extension', 'Overhead Triceps Extension'),
        ('Dips', 'Dips'),
        ('Triceps Kick Backs', 'Triceps Kick Backs'),
        ('Hammer Curl', 'Hammer Curl'),
        ('Inner Biceps Curl', 'Inner Biceps Curl'),
        ('Bar Curl', 'Bar Curl'),
        ('Wrist Curl', 'Wrist Curl')
    )
    ARM_EX = models.CharField(

        choices=TYPE,
        max_length = 30,
        # null=True,
    )
    AMOUNT = models.CharField(max_length=70)
    def __str__(self):
        return ('"{}", "{}"').format(self.ARM_EX,self.AMOUNT)
    class Meta:
        verbose_name = "Workout Arms"
        verbose_name_plural = "Workout Arms"

class WorkoutLegs(models.Model):
    user= models.ForeignKey(User,on_delete=models.CASCADE)
    date= models.DateTimeField(default=timezone.now)

    TYPE = (
        ('Squat', 'Squat'),
        ('Walking_Lunge', 'Walking_Lunge'),
        ('Calf_Raises', 'Calf_Raises'),
        ('Push_Ups', 'Push_Ups'),
        ('Hip_Thrust', 'Hip_Thrust'),
        ('Hip_Abduction', 'Hip_Abduction'),

    )
    AMOUNT = models.CharField(max_length=70)
    LEG_EX = models.CharField(
        choices=TYPE,
        max_length = 30,
        null=True,
        default='None',
    )
    def __str__(self):
        return ('"{}", "{}"').format(self.LEG_EX,self.AMOUNT)
    class Meta:
        verbose_name = "Workout Legs"
        verbose_name_plural = "Workout Legs"

class Workout(models.Model):

    user= models.ForeignKey(User,on_delete=models.CASCADE)
    date= models.DateTimeField(default=timezone.now)
    TYPE_BACK = (
        ('Trapezius_Shrug', 'Trapezius Shrug'),
        ('Reverse_Fly', 'Reverse Fly'),
        ('Dumbell_Row', 'Dumbell Row'),
        ('Roman_Chair', 'Roman Chair'),
    )
    BACK_EX = models.CharField(
        choices=TYPE_BACK,
        max_length = 30,
        blank=True

    )
    TYPE_CHEST = (
        ('Bench_Press', 'Bench Press'),
        ('Dumbell_Press', 'Dumbell Press'),
        ('Fly', 'Fly'),
        ('Push_Ups', 'Push Ups'),
    )
    CHEST_EX = models.CharField(
        choices=TYPE_CHEST,
        max_length = 30,
        blank=True

    )
    TYPE_ARM = (
        ('Shoulder_Raise', 'Shoulder Raise'),
        ('Shoulder_Press', 'Shoulder Press'),
        ('Overhead_Triceps Extension', 'Overhead Triceps Extension'),
        ('Dips', 'Dips'),
        ('Triceps_Kick_Backs', 'Triceps Kick Backs'),
        ('Hammer_Curl', 'Hammer Curl'),
        ('Inner_Biceps_Curl', 'Inner Biceps Curl'),
        ('Bar_Curl', 'Bar Curl'),
        ('Wrist_Curl', 'Wrist Curl')
    )
    ARM_EX = models.CharField(
        choices=TYPE_ARM,
        max_length = 30,
        blank=True

    )

    TYPE_LEGS = (
        ('Squat', 'Squat'),
        ('Walking_Lunge', 'Walking Lunge'),
        ('Calf_Raises', 'Calf Raises'),
        ('Push_Ups_Leg', 'Push Ups'),
        ('Hip_Thrust', 'Hip Thrust'),
        ('Hip_Abduction', 'Hip Abduction'),

    )
    AMOUNT = models.CharField(max_length=70)
    LEG_EX = models.CharField(
        choices=TYPE_LEGS,
        max_length = 30,
        blank=True
   
    )
    AMOUNT = models.CharField(max_length=70)

    def __str__(self):
        return ('{} - {}').format(str(self.date)[:10], self.AMOUNT)


    