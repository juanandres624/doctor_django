import calendar
from django.db import models
from accounts.models import Account

class Calendar(models.Model):

    months = (
       ('Enero', 'Enero'), ('Febrero', 'Febrero'), ('Marzo', 'Marzo'),
       ('Abril', 'Abril'), ('Mayo', 'Mayo'), ('Junio', 'Junio'),
       ('Julio', 'Julio'), ('Agosto', 'Agosto'), ('Septiembre', 'Septiembre'),
       ('Octubre', 'Octubre'), ('Noviembre', 'Noviembre'), ('Diciembre', 'Diciembre'),
    )

    calendar_total_days = models.IntegerField()
    calendar_month = models.CharField(max_length=20, choices=months)
    calendar_year = models.IntegerField()
    is_active = models.BooleanField(default=True)
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.calendar_month


class CalendarDayAppointment(models.Model):
    calendar_id = models.ForeignKey(Calendar, on_delete=models.CASCADE)
    day_number = models.IntegerField()
    app_start_time = models.TimeField()
    app_end_time = models.TimeField()
    is_active = models.BooleanField(default=True)
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.calendar_id.__str__() + ' ' + str(self.app_start_time) + '-' + str(self.app_end_time)


class Appointment(models.Model):
    calendar_day_id = models.ForeignKey(CalendarDayAppointment, on_delete=models.CASCADE)
    user = models.ForeignKey(Account, on_delete=models.CASCADE, null=True)
    is_active = models.BooleanField(default=True)
    date_added = models.DateField(auto_now_add=True)
