from django.db import models

from django.db import models

class Equipment(models.Model):
    equipment_id = models.AutoField(primary_key=True)
    equipment_name = models.CharField(max_length=100)
    sport_name = models.CharField(max_length=100)
    available_count = models.IntegerField()
    booked_count = models.IntegerField()

class Booking(models.Model):
    booking_id = models.AutoField(primary_key=True)
    student_id = models.IntegerField()
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    booking_time = models.DateTimeField()
    status = models.CharField(max_length=10, choices=[('booked', 'Booked'), ('cancelled', 'Cancelled')])


