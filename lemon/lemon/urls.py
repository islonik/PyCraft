# urls.py in lemon app
from django.urls import path, include
from lemon.views import BookingView

from . import api
from . import views

urlpatterns = [
    # path("api/v1/menu-items",               api.meals,               name="meals"),
    path("api/v1/menu-items",               api.MealsView.as_view()),
    path("api/v1/menu-items/<int:pk>/",     api.MealView.as_view()),
    path("",                                views.index,             name='index'),
    path("index/",                          views.index,             name='index'),
    path('about/',                          views.about,             name='about'),
    path('menu/',                           views.menu,              name='menu'),
    path('menu_item/<int:pk>/',             views.menu_item,         name="menu_item"),
    path('booking/',                        BookingView.as_view(),   name="booking"),
    path('bookings/',                       views.bookings,          name='bookings'),

    path('__debug__', include('debug_toolbar.urls')),
]