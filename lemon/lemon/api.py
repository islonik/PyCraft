# views.py in lemon app
from django.db import IntegrityError
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework import status, serializers, generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView

from .models import Meal
from .serializers import MealSerializer

# Create your API here.

# Function-based view
@api_view(['GET'])
def meals(request):
    meals = Meal.objects.all().values();
    return Response(
        {"meals": list(meals)},
        status=status.HTTP_200_OK
    )

# Class-based view
class MealView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer
    # def get(self, request, pk):
    #     try:
    #         item = Meal.objects.get(pk=pk);
    #     except Meal.DoesNotExist:
    #         print("Meal object doesn't exist for pk = {}".format(pk))
    #         item = ""
    #     serializer = MealSerializer(item, many=False)
    #     return Response(
    #         {"meal": serializer.data },
    #         status=status.HTTP_200_OK
    #     )