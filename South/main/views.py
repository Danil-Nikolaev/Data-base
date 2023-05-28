from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from django.views import View
from django.views.generic import ListView, TemplateView
from django.views.generic import DetailView

from main.models import Appointments, Rates, Rooms, Filials, Doctors, Reservations,Meals,Patients,Procedures, LocalSqlQueries

from django.db.models.fields import Field



class PatientsWithAppointment(TemplateView):
    template_name = 'main/list_query/list_patient_with_appointment.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["models"] = LocalSqlQueries.patients_with_appointment()
        name_fields = ['id', 'first_name', 'last_name', 'birthdate', 'gender', 'address', 'phone_number', 'email', 
                       'room_id', 'doctor_id', 'reservation_id', 'appointment_id', 'meal_id', 'filial_id', 'rate_id']
        context['name_fields'] = name_fields
        return context
    


class ProcedureHighPrice(TemplateView):
    template_name = 'main/list_query/list_procedure_high_price.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["models"] = LocalSqlQueries.procedure_high_price()
        name_fields = ['id', 'procedure_name', 'description', 'price']
        context['name_fields'] = name_fields
        return context


class DoctorsHigh(TemplateView):
    template_name = 'main/list_query/list_doctors_high.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["models"] = LocalSqlQueries.doctors_high()
        name_fields = ['id', 'first_name', 'last_name', 'specialization', 'phone_number', 'email']
        context['name_fields'] = name_fields
        return context


class DoctorsWithAppointment(TemplateView):
    template_name = 'main/list_query/list_doctors_high.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["models"] = LocalSqlQueries.doctors_with_appointment()
        name_fields = ['id', 'first_name', 'last_name', 'specialization', 'phone_number', 'email']
        context['name_fields'] = name_fields
        return context


class PatientsWithHighPriceProcedure(TemplateView):
    template_name = 'main/list_query/list_patient_with_appointment.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["models"] = LocalSqlQueries.patients_with_high_price_procedure()
        name_fields = ['id', 'first_name', 'last_name', 'birthdate', 'gender', 'address', 'phone_number', 'email', 
                       'room_id', 'doctor_id', 'reservation_id', 'appointment_id', 'meal_id', 'filial_id', 'rate_id']
        context['name_fields'] = name_fields
        return context


class ProcedureWithoutAppointment(TemplateView):
    template_name = 'main/list_query/list_procedure_high_price.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["models"] = LocalSqlQueries.procedure_without_appointment()
        name_fields = ['id', 'procedure_name', 'description', 'price']
        context['name_fields'] = name_fields
        return context


class PatientsLowCapacity(TemplateView):
    template_name = 'main/list_query/list_patient_with_appointment.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["models"] = LocalSqlQueries.patients_low_capacity()
        name_fields = ['id', 'first_name', 'last_name', 'birthdate', 'gender', 'address', 'phone_number', 'email', 
                       'room_id', 'doctor_id', 'reservation_id', 'appointment_id', 'meal_id', 'filial_id', 'rate_id']
        context['name_fields'] = name_fields
        return context


class MainView(View):
    template_name = 'main/index.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

# ==========================LISTS==============================

class ListProcedures(ListView):
    template_name = 'main/list/list_services.html'
    model = Procedures
    context_object_name = 'models'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['fields'] = self.model._meta.get_fields()
        name_fields = ['id', 'procedure_name', 'description', 'price']
        context['name_fields'] = name_fields
        return context  


class ListRates(ListView):
    template_name = 'main/list/list_rates.html'
    model = Rates
    context_object_name = 'models'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['fields'] = self.model._meta.get_fields()
        name_fields = ['rate_id', 'rate_name', 'description', 'price']
        context['name_fields'] = name_fields
        return context  


class ListRooms(ListView):
    template_name = 'main/list/list_rooms.html'
    model = Rooms
    context_object_name = 'models'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['fields'] = self.model._meta.get_fields()
        name_fields = ['room_id', 'room_number', 'room_type', 'capacity', 'busy']
        context['name_fields'] = name_fields
        return context  


class ListFilials(ListView):
    template_name = 'main/list/list_filials.html'
    model = Filials
    context_object_name = 'models'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['fields'] = self.model._meta.get_fields()
        name_fields = ['id', 'filial_name', 'address', 'phone_number']
        context['name_fields'] = name_fields
        return context  


class ListPatients(ListView):
    template_name = 'main/list/list_clients.html'
    model = Patients
    context_object_name = 'models'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['fields'] = self.model._meta.get_fields()
        name_fields = ['id', 'first_name', 'last_name', 'birthdate', 'gender', 'address', 'phone_number', 'email', 
                       'room_id', 'doctor_id', 'reservation_id', 'appointment_id', 'meal_id', 'filial_id', 'rate_id']
        context['name_fields'] = name_fields
        return context  


class ListReservations(ListView):
    template_name = 'main/list/list_reservations.html'
    model = Reservations
    context_object_name = 'models'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['fields'] = self.model._meta.get_fields()
        name_fields = ['id', 'check_in_date', 'check_out_date', 'total_price']
        context['name_fields'] = name_fields
        return context   


class ListAppointments(ListView):
    template_name = 'main/list/list_appointments.html'
    model = Appointments
    context_object_name = 'models'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['fields'] = self.model._meta.get_fields()
        name_fields = ['id', 'doctor_id', 'procedure_id', 'appointment_date', 'appointment_time']
        context['name_fields'] = name_fields
        return context  


class ListMeals(ListView):
    template_name = 'main/list/list_meals.html'
    model = Meals
    context_object_name = 'models'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['fields'] = self.model._meta.get_fields()
        name_fields = ['id', 'meal_type', 'description', 'price']
        context['name_fields'] = name_fields
        return context  


class ListDoctors(ListView):
    template_name = 'main/list/list_doctors.html'
    model = Doctors
    context_object_name = 'models'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['fields'] = self.model._meta.get_fields()
        name_fields = ['id', 'first_name', 'last_name', 'specialization', 'phone_number', 'email']
        context['name_fields'] = name_fields
        return context   

