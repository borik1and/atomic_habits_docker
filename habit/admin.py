from django.contrib import admin

from habit.models import Habit


@admin.register(Habit)
class HabitAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'action', 'place', 'lead_time', 'sign_pleasant_habit', 'related_habit', 'period',
                    'reward', 'time_to_complete')
