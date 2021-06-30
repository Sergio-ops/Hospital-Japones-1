from datetime import datetime
from django import forms
from django.core.checks.messages import Error
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.translation import activate
from django.views.generic import ListView, CreateView, UpdateView
from .forms import HistoriCForms
from ..paciente.models import Paciente
from ..evolucion.models import Evolucion
from .models import HistoriaClinica
from ..examenfisico.models import ExamenFisico
from django.db import transaction
from django.urls.base import reverse_lazy



"""Utilizamos el modelo de Evolucion ya que la primer Hisotria Clinica
es la PRIMER evolucion"""
class IndexHistoriaClinica(LoginRequiredMixin,ListView):
    model = HistoriaClinica
    template_name = "historiaapp/index.html"
    
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    


class CreateHistoriaClinica(LoginRequiredMixin,CreateView):
    model = HistoriaClinica
    form_class = HistoriCForms
    template_name = "historiaapp/create.html"
    success_url = reverse_lazy("indexHistoriaC")

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
        
    
    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == "historia_add":
                try:
                    with transaction.atomic():
                        paciente = Paciente()
                        paciente.nombre = request.POST['nombre']
                        paciente.apellido_paterno = request.POST['apellido_paterno']
                        paciente.apellido_materno  = request.POST['apellido_materno']
                        paciente.edad  = request.POST['edad']
                        paciente.nro_documento = request.POST['nro_documento']
                        paciente.sexo = request.POST['sexo']
                        paciente.fecha_nacimiento = request.POST['fecha_nacimiento']
                        paciente.ocupacion = request.POST['ocupacion']
                        paciente.estado_civil = request.POST['estado_civil']
                        paciente.residencia = request.POST['residencia']
                        paciente.procedencia = request.POST['procedencia']
                        paciente.domicilio = request.POST['domicilio']
                        paciente.save()

                        historia = HistoriaClinica()
                        historia.id_pacienteFK_id = paciente.id_pacientePK
                        historia.id_medicoFK_id = request.POST['id_medicoFK']
                        historia.cod_historiaclinica = request.POST['cod_historiaclinica']
                        historia.fecha_ingresohospital = request.POST['fecha_ingresohospital']
                        historia.fecha_ingresodomo = request.POST['fecha_ingresodomo']
                        historia.grado_instruccion = request.POST['grado_instruccion']
                        historia.proviene = request.POST['proviene']
                        historia.antecedente = request.POST['antecedente']
                        historia.historia_enfermedad_actual = request.POST['historia_enfermedad_actual']
                        historia.tension_arterial = request.POST['tension_arterial']
                        historia.frecuencia_cardiaca = request.POST['frecuencia_cardiaca']
                        historia.temp_ax = request.POST['temp_ax']
                        historia.frecuencia_respiratoria = request.POST['frecuencia_respiratoria']
                        historia.sindrome_at = request.POST['sindrome_at']
                        historia.peso = request.POST['peso']
                        historia.piel_mucosa = request.POST['piel_mucosa']
                        historia.neurologico = request.POST['neurologico']
                        historia.cardiopulmonar = request.POST['cardiopulmonar']
                        historia.abdomen = request.POST['abdomen']
                        historia.genitourinario = request.POST['genitourinario']
                        historia.musculoesqueletico = request.POST['musculoesqueletico']
                        historia.impresion_diagnostica = request.POST['impresion_diagnostica']
                        historia.save()

                        evolucion = Evolucion()
                        evolucion.id_historiaclinicaFK_id = historia.id_historiaPK
                        evolucion.id_medicoFK_id = historia.id_medicoFK_id
                        evolucion.fecha_hora = datetime.now()
                        evolucion.save()

                except Exception as e:
                    data['error'] = 'Error al procesar la solicitud: ' + str(e)
                    print(data['error'])
        except Exception as e:
            data['error'] = 'Error al procesar la solicitud: ' + str(e)
            print(data['error'])
        return redirect('indexHistoriaC')
        

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['action'] = "historia_add"
        return context


class UpdateHistoriaClinica(UpdateView):
    model = HistoriaClinica
    form_class = HistoriCForms
    template_name = 'historiaapp/update.html'

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['label_boton'] = 'Confirmar los datos nuevos'
        return context
    
    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'historia_edit':
                data = []
                try:
                    with transaction.atomic():
                        
                        paciente = Paciente.objects.get(pk = self.get_object().id_pacienteFK_id)
                        paciente.nombre = request.POST['nombre']
                        paciente.apellido_paterno = request.POST['apellido_paterno']
                        paciente.apellido_materno  = request.POST['apellido_materno']
                        paciente.edad  = request.POST['edad']
                        paciente.nro_documento = request.POST['nro_documento']
                        paciente.sexo = request.POST['sexo']
                        paciente.fecha_nacimiento = request.POST['fecha_nacimiento']
                        paciente.ocupacion = request.POST['ocupacion']
                        paciente.estado_civil = request.POST['estado_civil']
                        paciente.residencia = request.POST['residencia']
                        paciente.procedencia = request.POST['procedencia']
                        paciente.domicilio = request.POST['domicilio']
                        paciente.save()

                        historia = HistoriaClinica.objects.get(pk = self.get_object().id_historiaPK)
                        historia.id_pacienteFK_id = paciente.id_pacientePK
                        historia.id_medicoFK_id = request.POST['id_medicoFK']
                        historia.cod_historiaclinica = request.POST['cod_historiaclinica']
                        historia.fecha_ingresohospital = request.POST['fecha_ingresohospital']
                        historia.fecha_ingresodomo = request.POST['fecha_ingresodomo']
                        historia.grado_instruccion = request.POST['grado_instruccion']
                        historia.proviene = request.POST['proviene']
                        historia.antecedente = request.POST['antecedente']
                        historia.historia_enfermedad_actual = request.POST['historia_enfermedad_actual']
                        historia.tension_arterial = request.POST['tension_arterial']
                        historia.frecuencia_cardiaca = request.POST['frecuencia_cardiaca']
                        historia.temp_ax = request.POST['temp_ax']
                        historia.frecuencia_respiratoria = request.POST['frecuencia_respiratoria']
                        historia.sindrome_at = request.POST['sindrome_at']
                        historia.peso = request.POST['peso']
                        historia.piel_mucosa = request.POST['piel_mucosa']
                        historia.neurologico = request.POST['neurologico']
                        historia.cardiopulmonar = request.POST['cardiopulmonar']
                        historia.abdomen = request.POST['abdomen']
                        historia.genitourinario = request.POST['genitourinario']
                        historia.musculoesqueletico = request.POST['musculoesqueletico']
                        historia.impresion_diagnostica = request.POST['impresion_diagnostica']
                        historia.save()

                except Exception as e:
                    data['error'] = str(e)
                    print(str(e))
        except Exception as e:
            data['error'] = str(e)
            print(str(e))
        
        return redirect('indexHistoriaC')


