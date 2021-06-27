from django.shortcuts import render
from django.views.generic import ListView
from .models import Paciente
from ..medico.models import Medico

class PacienteList(ListView):
    model = Medico
    template_name = 'indexpaciente.html'
