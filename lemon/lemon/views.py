# views.py in lemon app
from django.shortcuts import render
from django.http import HttpResponse
from lemon.forms import BookingForm

# Create your views here.

def index(request):
    return HttpResponse("Hello World From <h2>Lemon</h2> View!")

def booking(request):
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid:
            form.save()
    context = {"form": form}
    return render(request, "booking.html", context)

def menu(request):
    context = {"menu": "A drifter claiming to be a Galaxy Ranger. Her true name is unknown, and she walks the cosmos alone, carrying with her a long sword." }
    return render(request, "menu.html", context)

def about(request):
    context = {"about": "Little Lemon is a family-owned Mediterranean restaurant, focused on traditional recipes served with a modern twist. The chefs draw inspiration from Italian, Greek, and Turkish culture and have a menu of 12–15 items that they rotate seasonally. The restaurant has a rustic and relaxed atmosphere with moderate prices, making it a popular place for a meal any time of the day." }
    return render(request, "about.html", context)