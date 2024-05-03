# urls.py in lemon app
from django.urls import path, include
from lemon.views import BookingView

from .api.menu_items import MealView, MealsView
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    #-------------------------
    # reused API
    #-------------------------
    # could be used to generate an authentication token for a user
    path("api/api-token-auth",              obtain_auth_token),
    #-------------------------
    # API
    #-------------------------
    path("api/v1/menu-items",               MealsView.as_view()),
    path("api/v1/menu-items/<int:pk>/",     MealView.as_view(),  name='menu-item-view'),

    #-------------------------
    # HTML templates
    #-------------------------
    path("",                                views.index,             name='index'),
    path("index/",                          views.index,             name='index'),
    path('about/',                          views.about,             name='about'),
    path('menu/',                           views.menu,              name='menu'),
    path('menu-item/<int:pk>/',             views.menu_item,         name="menu-item"),
    path('booking/',                        BookingView.as_view(),   name="booking"),
    path('bookings/',                       views.bookings,          name='bookings'),

    path('__debug__', include('debug_toolbar.urls')),
]