
from rest_framework import status, serializers, generics
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from rest_framework.response import Response

from ..models import Booking

from ..serializers import BookingSerializer

#-------------------------
# API:
#
# /api/bookings - Customer - GET    - Returns bookings.
# /api/bookings - Customer - POST   - Adds a new booking.
# /api/bookings - Customer - DELETE - Deletes bookings.
#-------------------------
@permission_classes([IsAuthenticated])
class BookingsView(generics.CreateAPIView, generics.ListAPIView, generics.DestroyAPIView):
    throttle_classes = [AnonRateThrottle, UserRateThrottle]
    # limit HTTP methods
    http_method_names = ['get', 'post', 'delete']

    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication,]
    ordering_fields = ['reservation_date', 'reservation_time']
