# Generated by Django 3.2.8 on 2021-11-04 20:55

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('workout_names', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Workout_name',
            new_name='WorkoutName',
        ),
    ]
