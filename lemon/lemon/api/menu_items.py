# api/menu_items.py in lemon app
from django.core.exceptions import PermissionDenied
from django.db import IntegrityError
from django.http import JsonResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt

from rest_framework import status, serializers, generics
from rest_framework.authentication import BasicAuthentication, TokenAuthentication, SessionAuthentication
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from rest_framework.views import APIView


from ..models import Cuisine, Meal
from ..serializers import MealSerializer

# Create your API here.

#-----------------------------
# Function-based views
#-----------------------------
# @api_view(['GET'])
# def meals(request):
#     meals = Meal.objects.all().values();
#     return Response(
#         meals,
#         status=status.HTTP_200_OK
#     )
def access_denied():
    return HttpResponseForbidden("Access denied. You are not a manager")

#-----------------------------
# Class-based views
#-----------------------------
@permission_classes([IsAuthenticated])
class MealsView(generics.CreateAPIView, generics.ListAPIView):
    throttle_classes = [AnonRateThrottle, UserRateThrottle]
    # limit HTTP methods
    http_method_names = ['get', 'put', 'post', 'patch', 'delete']
    queryset = Meal.objects.all()
    serializer_class = MealSerializer
    # specifies used authentication classes
    authentication_classes = [TokenAuthentication, SessionAuthentication,]
    # searching
    search_fields = ['name', 'desc']
    # ordering
    ordering_fields = ['id', 'price']

    def put(self, request, *args, **kwargs):
        return access_denied()

    def post(self, request, *args, **kwargs):
        if (request.user.groups.filter(name='Manager')).exists():
            return self.create(request, *args, **kwargs)
        else:
            return access_denied()

    def patch(self, request, *args, **kwargs):
        return access_denied()

    def delete(self, request, *args, **kwargs):
        return access_denied()

@permission_classes([IsAuthenticated])
class MealView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    throttle_classes = [AnonRateThrottle, UserRateThrottle]
    # limit HTTP methods
    http_method_names = ['get', 'put', 'patch', 'delete']
    queryset = Meal.objects.all()
    serializer_class = MealSerializer
    # specifies used authentication classes
    authentication_classes = [TokenAuthentication, SessionAuthentication,]

    def put(self, request, *args, **kwargs):
        if (request.user.groups.filter(name='Manager')).exists():
            return super().put(request, *args, **kwargs)
        else:
            return access_denied()

    def patch(self, request, *args, **kwargs):
        if (request.user.groups.filter(name='Manager')).exists():
            return super().patch(request, *args, **kwargs)
        else:
            return access_denied()

    def delete(self, request, *args, **kwargs):
        if (request.user.groups.filter(name='Manager')).exists():
            return super().delete(request, *args, **kwargs)
        else:
            return access_denied()
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