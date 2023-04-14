from django.urls import path
from main.views import MainView

from . import views

urlpatterns = [
    path('', MainView.as_view()),
]