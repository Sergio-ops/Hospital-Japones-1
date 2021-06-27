from django.urls import path
from .views import PacienteList

urlpatterns = [
    path('list', PacienteList.as_view(),name='ListaPaciente')
]