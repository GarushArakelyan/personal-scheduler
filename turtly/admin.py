from django.contrib import admin
from .models import Entry, WorkoutBack, WorkoutArms, WorkoutChest, WorkoutLegs, Workout
# Register your models here.
admin.site.register(Entry)
admin.site.register(Workout)
