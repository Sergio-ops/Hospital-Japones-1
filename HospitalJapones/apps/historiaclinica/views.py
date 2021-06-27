from django.core.checks.messages import Error
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView
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
    template_name = "historiaclinicaapp/index.html"
    
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class CreateHistoriaClinica(LoginRequiredMixin,CreateView):
    model = HistoriaClinica
    form_class = HistoriCForms
    template_name = "historiaclinicaapp/create.html"
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
                        historia.impresion_diagnostica = request.POST['impresion_diagnostica']
                        historia.save()

                        examenfisico = ExamenFisico()
                        examenfisico.tension_arterial = request.POST['tension_arterial']
                        examenfisico.frecuencia_cardiaca = request.POST['frecuencia_cardiaca']
                        examenfisico.frecuencia_respiratoria = request.POST['frecuencia_respiratoria']
                        examenfisico.temp_ax = request.POST['temp_ax']
                        examenfisico.sindrome_at = request.POST['sindrome_at']
                        examenfisico.fio = request.POST['fio']
                        examenfisico.pam = request.POST['pam']
                        examenfisico.avm = request.POST['avm']
                        examenfisico.modo = request.POST['modo']
                        examenfisico.noradrenalina = request.POST['noradrenalina']
                        examenfisico.atracurio = request.POST['atracurio']
                        examenfisico.vc = request.POST['vc']
                        examenfisico.peep = request.POST['peep']
                        examenfisico.prono_dias = request.POST['prono_dias']
                        examenfisico.pao_fio = request.POST['pao_fio']
                        examenfisico.pi = request.POST['pi']
                        examenfisico.peso = request.POST['peso']
                        examenfisico.piel_mucosa = request.POST['piel_mucosa']
                        examenfisico.neurologico = request.POST['neurologico']
                        examenfisico.cardiopulmonar = request.POST['cardiopulmonar']
                        examenfisico.abdomen = request.POST['abdomen']
                        examenfisico.genitourinario = request.POST['genitourinario']
                        examenfisico.musculoesqueletico = request.POST['musculoesqueletico']
                        examenfisico.save()

                        evolucion = Evolucion()
                        evolucion.id_historiaclinicaFK_id = historia.id_historiaPK
                        evolucion.id_examenfisicoFK_id = examenfisico.id_examenfisicoPK
                        evolucion.id_medicoFK_id = request.POST['id_medicoPK']
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


        
