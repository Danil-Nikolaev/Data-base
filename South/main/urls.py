from django.urls import path
from main.views import MainView, ListBookings, ListClients, ListFilials, ListRates, ListRooms, ListServices
from main.views import OccupancyRate, Birthday, PopularTypeRooms, PopularRates, PopularFilialType, UnpopularFilial, ServicesInRates
from . import views

urlpatterns = [
    path('', MainView.as_view()),
    path('bookings/', ListBookings.as_view()),
    path('clients/', ListClients.as_view()),
    path('filials/', ListFilials.as_view()),
    path('rates/', ListRates.as_view()),
    path('rooms/', ListRooms.as_view()),
    path('services/', ListServices.as_view()),
    path('services/services_in_rates/', ServicesInRates.as_view()),
    path('rooms/occupancy_rate/', OccupancyRate.as_view()), 
    path('rooms/birthday/', Birthday.as_view()), 
    path('rooms/popular_type_rooms/', PopularTypeRooms.as_view()),
    path('rates/popular_rates/', PopularRates.as_view()),
    path('filials/popular_filial_type/', PopularFilialType.as_view()),
    path('filials/unpopular_filial/', UnpopularFilial.as_view())
]