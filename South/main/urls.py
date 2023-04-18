from django.urls import path
from main.views import MainView, ListBookings, ListClients, ListFilials, ListRates, ListRooms, ListServices, ListWorkers

from . import views

urlpatterns = [
    path('', MainView.as_view()),
    path('bookings/', ListBookings.as_view()),
    path('clients/', ListClients.as_view()),
    path('filials/', ListFilials.as_view()),
    path('rates/', ListRates.as_view()),
    path('rooms/', ListRooms.as_view()),
    path('services/', ListServices.as_view()),
    path('workers/', ListWorkers.as_view()),    
]