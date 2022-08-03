from django.contrib import admin
from .models import Calendar, CalendarDayAppointment, Appointment


class CalendarAdmin(admin.ModelAdmin):
    list_display = ('calendar_total_days', 'calendar_month', 'calendar_year', 'is_active')


class CalendarDayAppointmentAdmin(admin.ModelAdmin):
    list_display = ('calendar_id', 'day_number', 'app_start_time', 'app_end_time', 'is_active')


class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('calendar_day_id', 'user', 'is_active', 'date_added')


admin.site.register(Calendar, CalendarAdmin)
admin.site.register(CalendarDayAppointment, CalendarDayAppointmentAdmin)
admin.site.register(Appointment, AppointmentAdmin)
