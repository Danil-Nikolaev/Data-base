from django.urls import path
from main.views import MainView, ListFilials, ListRates, ListRooms, ListProcedures, ListReservations, ListPatients, ListDoctors, ListMeals, ListAppointments
from main.views import PatientsWithAppointment, ProcedureHighPrice, DoctorsHigh, DoctorsWithAppointment, PatientsWithHighPriceProcedure, ProcedureWithoutAppointment, PatientsLowCapacity
from . import views

urlpatterns = [
    path('', MainView.as_view()),
    
    path('reservations/', ListReservations.as_view()),
    path('clients/', ListPatients.as_view()),
    path('filials/', ListFilials.as_view()),
    path('rates/', ListRates.as_view()),
    path('rooms/', ListRooms.as_view()),
    path('services/', ListProcedures.as_view()),
    path('doctors/', ListDoctors.as_view()),
    path('meals/', ListMeals.as_view()),
    path('appointments/', ListAppointments.as_view()),

    path('PatientsWithAppointment/', PatientsWithAppointment.as_view()),
    path('ProcedureHighPrice/', ProcedureHighPrice.as_view()),
    path('DoctorsHigh/', DoctorsHigh.as_view()),
    path('DoctorsWithAppointment/', DoctorsWithAppointment.as_view()),
    path('PatientsWithHighPriceProcedure/', PatientsWithHighPriceProcedure.as_view()),
    path('ProcedureWithoutAppointment/', ProcedureWithoutAppointment.as_view()),
    path('PatientsLowCapacity/', PatientsLowCapacity.as_view())
]