from django.shortcuts import render
from .models import Equipment, Booking

def index(request):
    equipment_list = Equipment.objects.all()
    bookings = Booking.objects.all()
    return render(request, 'index.html', {'equipment_list': equipment_list, 'bookings': bookings})

