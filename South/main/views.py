from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from django.views import View
from django.views.generic import ListView, TemplateView
from django.views.generic import DetailView

from main.models import Services, Rates, Rooms, Filials, Clients, Bookings, LocalSqlQueries

from django.db.models.fields import Field


class OccupancyRate(TemplateView):
    template_name = 'main/list_query/list_occupancy_rate.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["model"] = LocalSqlQueries.occupancy_rate()
        return context
    


class Birthday(TemplateView):
    template_name = 'main/list_query/list_birthday.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["model"] = LocalSqlQueries.get_birthday_tommorow()
        return context


class PopularFilialType(TemplateView):
    template_name = 'main/list_query/list_popular_filial_type.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["model"] = LocalSqlQueries.get_popular_filial_type()
        return context


class PopularTypeRooms(TemplateView):
    template_name = 'main/list_query/list_popular_type_rooms.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["model"] = LocalSqlQueries.popular_type_rooms()
        return context


class PopularRates(TemplateView):
    template_name = 'main/list_query/list_popular_rates.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["model"] = LocalSqlQueries.popular_rates()
        return context


class UnpopularFilial(TemplateView):
    template_name = 'main/list_query/list_unpopular_filial.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["model"] = LocalSqlQueries.unpopular_filial()
        return context


class ServicesInRates(TemplateView):
    template_name = 'main/list_query/list_services_in_rates.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["model"] = LocalSqlQueries.services_in_rates_all()
        return context


class MainView(View):
    template_name = 'main/index.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)



class ListServices(ListView):
    template_name = 'main/list/list_services.html'
    model = Services
    context_object_name = 'models'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['fields'] = self.model._meta.get_fields()
        name_fields = ['service_id', 'title', 'description', 'price']
        context['name_fields'] = name_fields
        return context  


class ListRates(ListView):
    template_name = 'main/list/list_rates.html'
    model = Rates
    context_object_name = 'models'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['fields'] = self.model._meta.get_fields()
        name_fields = ['rate_id', 'title', 'description', 'price']
        context['name_fields'] = name_fields
        return context  


class ListRooms(ListView):
    template_name = 'main/list/list_rooms.html'
    model = Rooms
    context_object_name = 'models'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['fields'] = self.model._meta.get_fields()
        name_fields = ['room_id', 'number', 'type_number', 'busy', 'client']
        context['name_fields'] = name_fields
        return context  


class ListFilials(ListView):
    template_name = 'main/list/list_filials.html'
    model = Filials
    context_object_name = 'models'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['fields'] = self.model._meta.get_fields()
        name_fields = ['filial_id', 'title', 'address', 'phone', 'email']
        context['name_fields'] = name_fields
        return context  


class ListClients(ListView):
    template_name = 'main/list/list_clients.html'
    model = Clients
    context_object_name = 'models'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['fields'] = self.model._meta.get_fields()
        name_fields = ['client_id', 'name', 'birthday', 'gender', 'phone', 'email']
        context['name_fields'] = name_fields
        return context  


class ListBookings(ListView):
    template_name = 'main/list/list_bookings.html'
    model = Bookings
    context_object_name = 'models'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['fields'] = self.model._meta.get_fields()
        name_fields = ['booking', 'client', 'filial', 'arrival_date', 'departue_date', 'room', 'rate']
        context['name_fields'] = name_fields
        return context   
