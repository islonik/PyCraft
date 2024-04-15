# urls.py in lemon app
from django.urls import path
from lemon.views import BookingView

from . import views

urlpatterns = [
    path("",                    views.index,             name='index'),
    path("index/",              views.index,             name='index'),
    path('about/',              views.about,             name='about'),
    path('menu/',               views.menu,              name='menu'),
    path('menu_item/<int:pk>/', views.menu_item,         name="menu_item"),
    path('booking/',            BookingView.as_view(),   name="booking"),
    path('bookings/',           views.bookings,          name='bookings'),
]