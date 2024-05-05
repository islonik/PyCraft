# urls.py in lemon app
from django.urls import path, include
from lemon.views import BookingView

from .api.menu_items import MealView, MealsView
from .api.user_groups import ManagersView, ManagerView, DeliveryCrewView, DeliveryPersonView
#from .api.user_groups import manager_view
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
    path("api/menu-items",                           MealsView.as_view()),
    path("api/menu-items/<int:pk>/",                 MealView.as_view(),           name='menu-item-view'),
    path("api/groups/manager/users",                 ManagersView.as_view()),
    path("api/groups/manager/users/<int:pk>/",       ManagerView.as_view(),        name='manager-view'),
    path("api/groups/delivery-crew/users",           DeliveryCrewView.as_view()),
    path("api/groups/delivery-crew/users/<int:pk>/", DeliveryPersonView.as_view(), name='delivery-person-view'),

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