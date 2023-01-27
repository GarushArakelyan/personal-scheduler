# Generated by Django 2.1.5 on 2023-01-27 17:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Study_Type_Entries', models.CharField(choices=[('PRG', 'Programming'), ('ADM', 'Admin'), ('DEV', 'DevOps'), ('LNG', 'Language'), ('OTH', 'Other')], default=None, max_length=3, null=True)),
                ('topic', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('completed', models.BooleanField(default=False)),
                ('link', models.CharField(max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Entry',
                'verbose_name_plural': 'Entries',
            },
        ),
        migrations.CreateModel(
            name='Workout',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('BACK_EX', models.CharField(blank=True, choices=[('Trapezius_Shrug', 'Trapezius Shrug'), ('Reverse_Fly', 'Reverse Fly'), ('Dumbell_Row', 'Dumbell Row'), ('Roman_Chair', 'Roman Chair')], max_length=30)),
                ('CHEST_EX', models.CharField(blank=True, choices=[('Bench_Press', 'Bench Press'), ('Dumbell_Press', 'Dumbell Press'), ('Fly', 'Fly'), ('Push_Ups', 'Push Ups')], max_length=30)),
                ('ARM_EX', models.CharField(blank=True, choices=[('Shoulder_Raise', 'Shoulder Raise'), ('Shoulder_Press', 'Shoulder Press'), ('Overhead_Triceps Extension', 'Overhead Triceps Extension'), ('Dips', 'Dips'), ('Triceps_Kick_Backs', 'Triceps Kick Backs'), ('Hammer_Curl', 'Hammer Curl'), ('Inner_Biceps_Curl', 'Inner Biceps Curl'), ('Bar_Curl', 'Bar Curl'), ('Wrist_Curl', 'Wrist Curl')], max_length=30)),
                ('LEG_EX', models.CharField(blank=True, choices=[('Squat', 'Squat'), ('Walking_Lunge', 'Walking Lunge'), ('Calf_Raises', 'Calf Raises'), ('Push_Ups_Leg', 'Push Ups'), ('Hip_Thrust', 'Hip Thrust'), ('Hip_Abduction', 'Hip Abduction')], max_length=30)),
                ('AMOUNT', models.CharField(max_length=70)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='WorkoutArms',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('ARM_EX', models.CharField(choices=[('SHL_RS', 'Shoulder Raise'), ('Shoulder Press', 'Shoulder Press'), ('Overhead Triceps Extension', 'Overhead Triceps Extension'), ('Dips', 'Dips'), ('Triceps Kick Backs', 'Triceps Kick Backs'), ('Hammer Curl', 'Hammer Curl'), ('Inner Biceps Curl', 'Inner Biceps Curl'), ('Bar Curl', 'Bar Curl'), ('Wrist Curl', 'Wrist Curl')], max_length=30)),
                ('AMOUNT', models.CharField(max_length=70)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Workout Arms',
                'verbose_name_plural': 'Workout Arms',
            },
        ),
        migrations.CreateModel(
            name='WorkoutBack',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('BACK_EX', models.CharField(choices=[('Trapezius Shrug', 'Trapezius Shrug'), ('Reverse Fly', 'Reverse Fly'), ('Dumbell Row', 'Dumbell Row'), ('Roman Chair', 'Roman Chair')], default=None, max_length=30, null=True)),
                ('AMOUNT', models.CharField(max_length=70)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Workout Back',
                'verbose_name_plural': 'Workout Back',
            },
        ),
        migrations.CreateModel(
            name='WorkoutChest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('CHEST_EX', models.CharField(choices=[('Bench Press', 'Bench Press'), ('Dumbell Press', 'Dumbell Press'), ('Fly', 'Fly'), ('Push Ups', 'Push Ups')], default=None, max_length=30, null=True)),
                ('AMOUNT', models.CharField(max_length=70)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Workout Chest',
                'verbose_name_plural': 'Workout Chest',
            },
        ),
        migrations.CreateModel(
            name='WorkoutLegs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('AMOUNT', models.CharField(max_length=70)),
                ('LEG_EX', models.CharField(choices=[('Squat', 'Squat'), ('Walking_Lunge', 'Walking_Lunge'), ('Calf_Raises', 'Calf_Raises'), ('Push_Ups', 'Push_Ups'), ('Hip_Thrust', 'Hip_Thrust'), ('Hip_Abduction', 'Hip_Abduction')], default='None', max_length=30, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Workout Legs',
                'verbose_name_plural': 'Workout Legs',
            },
        ),
    ]