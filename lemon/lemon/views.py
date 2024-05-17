# views.py in lemon app
from django.shortcuts import render
from django.utils import timezone
from django.views import View
from lemon.forms import BookingForm
from .models import Booking

# import model from API
from api.models import Meal

# Create your views here.

# Class-based view
class BookingView(View):
    def get(self, request):
        print("GET from BookingView...")

        booking = BookingForm()
        return self.render_new_booking(request, booking)

    def post(self, request):
        print("POST from BookingView...")

        booking = BookingForm(request.POST)
        if booking.is_valid:
            booking.save()
            # create new form
            booking = BookingForm()
        return self.render_new_booking(request, booking)

    @classmethod
    def render_new_booking(self, request, booking):
        context = {"form": booking}
        return render(request, "booking.html", context)

def bookings(request):
    booking_items = Booking.objects.all()
    items_dict = {"booking": booking_items}
    return render(request, "bookings.html", items_dict)

def index(request):
    return render(request, "index.html")

def menu(request):
    meal_items = Meal.objects.all()
    items_dict = {"menu": meal_items }
    return render(request, "menu.html", items_dict)

def menu_item(request, pk):
    try:
        item = Meal.objects.get(pk=pk);
    except Meal.DoesNotExist:
        print("Meal object doesn't exist for pk = {}".format(pk))
        item = ""
    item_dict = {"item": item }
    return render(request, "menu_item.html", item_dict)


def about(request):
    return render(request, "about.html")