from django import forms

from django.utils import timezone

from .models import Booking

class BookingForm(forms.ModelForm):
    # set initial values
    reservation_time = forms.DateField(initial = timezone.now().strftime("%Y-%m-%d"))

    class Meta:
        model = Booking
        fields = '__all__'

