# views.py in lemon app
from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from django.utils import timezone
from datetime import timedelta

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
            # javascript reset the form on the 'Success' in the beginning of the message
            first_name = booking.cleaned_data.get('first_name')
            last_name = booking.cleaned_data.get('last_name')
            return JsonResponse({
                'message': 'Success - Booking for {first_name} {last_name} completed!'.format(first_name=first_name, last_name=last_name)
            })
        return self.render_new_booking(request, booking)

    @classmethod
    def render_new_booking(self, request, booking):
        # Little Lemon doesn't provide booking more than for a week
        start_date = timezone.now()
        end_date = start_date + timedelta(days=7)
        # we provide up to 10 guests per day for booking
        total_available_places = 10
        # find total amount of guests for current day
        reservation_time = start_date.strftime("%Y-%m-%d")
        if request.GET.get('date'):
            reservation_time = request.GET.get('date')
        booking_items = Booking.objects.all().filter(reservation_time=reservation_time)
        total_guests = 0;
        for item in booking_items:
            total_guests += item.guest_count
        # find available places for booking
        max_guests = total_available_places - total_guests
        # find default amount of places for booking
        default_guests = 2
        if max_guests >= 2:
            default_guests = 2
        elif max_guests > 0:
            default_guests = 1
        else:
            default_guests = 0
        # set up min available places for booking
        min_guests = 1
        if default_guests == 0:
            min_guests = 0
        # create context for template
        context = {
            "form": booking,
            "reservation_time": reservation_time,
            "start_date": start_date.strftime("%Y-%m-%d"),
            "end_date": end_date.strftime("%Y-%m-%d"),
            "default_guests": default_guests,
            "min_guests" : min_guests,
            "max_guests" : max_guests,
        }
        return render(request, "booking.html", context)

def bookings(request):
    # show bookings between today and a week in advance
    start_date = timezone.now()
    end_date = start_date + timedelta(days=7)
    booking_items = Booking.objects.all().filter(reservation_time__gte=start_date.strftime("%Y-%m-%d"), reservation_time__lte=end_date.strftime("%Y-%m-%d"))
    items_dict = {"bookings": booking_items}
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