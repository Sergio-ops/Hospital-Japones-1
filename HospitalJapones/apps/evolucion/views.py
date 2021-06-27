from typing import List
from django.http import response, JsonResponse
from django.urls.base import reverse_lazy
from django.shortcuts import redirect, render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.base import View
from django.views.generic.edit import UpdateView
from .forms import EvolucionForms
from django.db import transaction
from datetime import date, datetime, timedelta

from django.views.generic import ListView, CreateView, DetailView, View
from ..historiaclinica.models import HistoriaClinica
from .models import Evolucion, det_cultivo_evolucion, det_tratmiento_evolucion
from ..cultivo.models import Cultivo
from ..medicamento.models import Medicamento
from ..examenfisico.models import ExamenFisico
from ..resultadolaboratorio.models import ResultadoLab
from HospitalJapones import settings
import json

#Lista de las evoluciones pertenecientes a una historia clinica (fk)
class EvolucionListFilterbyHC(ListView):
    model = Evolucion
    template_name = 'evolucionapp/index.html'

    def get_queryset(self):
        fk = self.kwargs['fk']
        return self.model.objects.filter(id_historiaclinicaFK = fk, estado = 'Activo')

def change_status(request):
    pk = request.POST.get('pk')
    evolucion = Evolucion.objects.get(id_evolucionPK=pk)
    evolucion.estado = 'Anulado'
    evolucion.save()
    id = evolucion.id_historiaclinicaFK_id
    data = id
    return response.HttpResponse(data)

#Crear Nueva Evolucion asociada a una historia clinica (fk)
class EvolucionDetailCreate(DetailView):
    model = Evolucion
    form_class = EvolucionForms
    template_name = 'evolucionapp/create.html'

    def get_object(self):
        id = self.kwargs.get("id")
        return get_object_or_404(Evolucion, id_evolucionPK=id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        fk = self.kwargs['id']
        historiaclinica = HistoriaClinica.objects.get(id_historiaPK = fk)
        fecha_ingreso = historiaclinica.fecha_ingresodomo
        fecha_actual = datetime.now()
        resultado = (fecha_actual - fecha_ingreso).days
        context['diasDomo'] = resultado
        return context 



    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == "search_medicamentos":
                data = []
                for i in Medicamento.objects.filter(nombre__icontains=request.POST['term']):
                    item = i.toJSON()
                    item['value'] = i.nombre
                    data.append(item)
            if action == "search_cultivos":
                data = []
                for i in Cultivo.objects.filter(nombre__icontains=request.POST['term']):
                    item = i.toJSON()
                    item['value'] = i.nombre
                    data.append(item)
            if action == "evolucion_add":
                try:
                    with transaction.atomic():
                        
                        cultivo_list = json.loads(request.POST['cultivos_list'])
                        medicamento_list = json.loads(request.POST['medicamento_list'])

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

                        laboratorio = ResultadoLab()
                        laboratorio.lab_gb = request.POST['lab_gb']
                        laboratorio.lab_hb = request.POST['lab_hb']
                        laboratorio.lab_ph = request.POST['lab_ph']
                        laboratorio.lab_got = request.POST['lab_got']
                        laboratorio.lab_neu = request.POST['lab_neu']
                        laboratorio.lab_htco = request.POST['lab_htco']
                        laboratorio.lab_pco = request.POST['lab_pco']
                        laboratorio.lab_gpt = request.POST['lab_gpt']
                        laboratorio.lab_lin = request.POST['lab_lin']
                        laboratorio.lab_cr = request.POST['lab_cr']
                        laboratorio.lab_hco = request.POST['lab_hco']
                        laboratorio.lab_pt = request.POST['lab_pt']
                        laboratorio.lab_cay = request.POST['lab_cay']
                        laboratorio.lab_urea = request.POST['lab_urea']
                        laboratorio.lab_alb = request.POST['lab_alb']
                        laboratorio.lab_po = request.POST['lab_po']
                        laboratorio.lab_plq = request.POST['lab_plq']
                        laboratorio.lab_na = request.POST['lab_na']
                        laboratorio.lab_eb = request.POST['lab_eb']
                        laboratorio.lab_cl = request.POST['lab_cl']
                        laboratorio.lab_k = request.POST['lab_k']
                        laboratorio.lab_lact = request.POST['lab_lact']
                        laboratorio.lab_dd = request.POST['lab_dd']
                        laboratorio.save()

                        evolucion = Evolucion()
                        evolucion.id_historiaclinicaFK_id = request.POST['id_historiaclinicaFK']
                        evolucion.id_medicoFK_id = request.POST['id_medicoPK']
                        evolucion.id_examenfisicoFK_id = examenfisico.id_examenfisicoPK
                        evolucion.id_resultadolabFK_id = laboratorio.id_resultadolabPK
                        evolucion.nro_cama = request.POST['nro_cama']
                        evolucion.dias_domo = request.POST['dias_domo']
                        evolucion.analisis = request.POST['analisis']
                        evolucion.plan = request.POST['plan']
                        evolucion.save()

                        for i in cultivo_list['cultivos']:
                            cultivo = Cultivo()
                            cultivo.nombre = i['nombre']
                            cultivo.save()

                            det = det_cultivo_evolucion()
                            det.id_cultivoFK_id = cultivo.id_cultivoPK
                            det.id_evolucionFK_id = evolucion.id_evolucionPK
                            det.fecha = date.today()
                            det.estado = "En curso"
                            det.save()

                        for i in medicamento_list['tratamiento']:
                            det_tratamiento = det_tratmiento_evolucion()
                            det_tratamiento.id_evolucionFK_id = evolucion.id_evolucionPK
                            det_tratamiento.id_medicamentoFK_id = i['id_medicamentoPK']
                            det_tratamiento.cantidad = i['cant']
                            det_tratamiento.indicacion = i['indicacion']
                            det_tratamiento.save()
                        data = {'id':evolucion.id_historiaclinicaFK_id}
                except Exception as e:
                    data['error'] = str(e)
                    print(str(e))
        except Exception as e:
            data['error'] = str(e)
            print(str(e))
        return JsonResponse(data,safe=False)


#Edita la evolucion seleccionada
class EvolucionUpdate(UpdateView):
    model = Evolucion
    form_class = EvolucionForms
    template_name = 'evolucionapp/update.html'


    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == "search_medicamentos":
                data = []
                for i in Medicamento.objects.filter(nombre__icontains=request.POST['term']):
                    item = i.toJSON()
                    item['value'] = i.nombre
                    data.append(item)
            if action == "search_cultivos":
                data = []
                for i in Cultivo.objects.filter(nombre__icontains=request.POST['term']):
                    item = i.toJSON()
                    item['value'] = i.nombre
                    data.append(item)
            if action == "evolucion_edit":
                try:
                    with transaction.atomic():
                        
                        cultivo_list = json.loads(request.POST['cultivos_list'])
                        medicamento_list = json.loads(request.POST['medicamento_list'])

                        examenfisico = ExamenFisico.objects.get(pk = self.get_object().id_examenfisicoFK_id)
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

                        laboratorio = ResultadoLab.objects.get(pk = self.get_object().id_resultadolabFK_id)
                        laboratorio.lab_gb = request.POST['lab_gb']
                        laboratorio.lab_hb = request.POST['lab_hb']
                        laboratorio.lab_ph = request.POST['lab_ph']
                        laboratorio.lab_got = request.POST['lab_got']
                        laboratorio.lab_neu = request.POST['lab_neu']
                        laboratorio.lab_htco = request.POST['lab_htco']
                        laboratorio.lab_pco = request.POST['lab_pco']
                        laboratorio.lab_gpt = request.POST['lab_gpt']
                        laboratorio.lab_lin = request.POST['lab_lin']
                        laboratorio.lab_cr = request.POST['lab_cr']
                        laboratorio.lab_hco = request.POST['lab_hco']
                        laboratorio.lab_pt = request.POST['lab_pt']
                        laboratorio.lab_cay = request.POST['lab_cay']
                        laboratorio.lab_urea = request.POST['lab_urea']
                        laboratorio.lab_alb = request.POST['lab_alb']
                        laboratorio.lab_po = request.POST['lab_po']
                        laboratorio.lab_plq = request.POST['lab_plq']
                        laboratorio.lab_na = request.POST['lab_na']
                        laboratorio.lab_eb = request.POST['lab_eb']
                        laboratorio.lab_cl = request.POST['lab_cl']
                        laboratorio.lab_k = request.POST['lab_k']
                        laboratorio.lab_lact = request.POST['lab_lact']
                        laboratorio.lab_dd = request.POST['lab_dd']
                        laboratorio.save()

                        evolucion = self.get_object()
                        evolucion.id_historiaclinicaFK_id = request.POST['id_historiaclinicaFK']
                        evolucion.id_medicoFK_id = request.POST['id_medicoPK']
                        evolucion.id_examenfisicoFK_id = examenfisico.id_examenfisicoPK
                        evolucion.id_resultadolabFK_id = laboratorio.id_resultadolabPK
                        evolucion.nro_cama = request.POST['nro_cama']
                        evolucion.dias_domo = request.POST['dias_domo']
                        evolucion.analisis = request.POST['analisis']
                        evolucion.plan = request.POST['plan']
                        evolucion.save()

                        evolucion.det_cultivo_evolucion_set.all().delete()
                        for i in cultivo_list['cultivos']:
                            cultivo = Cultivo()
                            cultivo.nombre = i['nombre']
                            cultivo.save()

                            det = det_cultivo_evolucion()
                            det.id_cultivoFK_id = cultivo.id_cultivoPK
                            det.id_evolucionFK_id = evolucion.id_evolucionPK
                            det.fecha = date.today()
                            det.estado = "En curso"
                            det.save()

                        evolucion.det_tratmiento_evolucion_set.all().delete()
                        for i in medicamento_list['tratamiento']:
                            det_tratamiento = det_tratmiento_evolucion()
                            det_tratamiento.id_evolucionFK_id = evolucion.id_evolucionPK
                            det_tratamiento.id_medicamentoFK_id = i['id_medicamentoPK']
                            det_tratamiento.cantidad = i['cant']
                            det_tratamiento.indicacion = i['indicacion']
                            det_tratamiento.save()
                        data = {'id':evolucion.id_historiaclinicaFK_id}
                except Exception as e:
                    data['error'] = str(e)
                    print(str(e))
        except Exception as e:
            data['error'] = str(e)
            print(str(e))
        return JsonResponse(data,safe=False)

    def get_detail_cultivo(self):
        data = []
        try:
            for i in det_cultivo_evolucion.objects.filter(id_evolucionFK_id=self.get_object().id_evolucionPK):
                item = i.id_cultivoFK.toJSON()
                item['fecha'] = str(i.fecha.strftime('%d-%m-%Y'))
                item['estado'] = i.estado
                data.append(item)
        except Exception as e:
            print(str(e))
        return data

    def get_detail_tratamiento(self):
        data = []
        try:
            for i in det_tratmiento_evolucion.objects.filter(id_evolucionFK_id=self.get_object().id_evolucionPK):
                item = i.id_medicamentoFK.toJSON()
                item['cant'] = i.cantidad
                item['indicacion'] = i.indicacion
                data.append(item)
        except Exception as e:
            print(str(e))
        return data

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['det_cultivo'] = json.dumps(self.get_detail_cultivo())
        context['det_tratamiento'] = json.dumps(self.get_detail_tratamiento())
        return context


class DetalleEvolucion(View):
    def get(self, request, *args, **kwargs):
        try:
            context = {
                'evolucion':Evolucion.objects.get(id_evolucionPK=self.kwargs['pk']),
                'logohospital': '{}{}'.format(settings.MEDIA_URL, 'logo-hospital.png'),
                'logogobernacion': '{}{}'.format(settings.MEDIA_URL, 'logo-gobernacion.png'),
                'direccion': '3er. Anillo Externo, Av. Japón, entre Av. Canal Cotoca y Av. Paraguá – Telef. Piloto: 3-462037',
                'ciudad': 'Santa Cruz de la Sierra - Bolivia',
            }
            return render(request,'evolucionapp/detalle.html',context)
        except Exception as e:
            print(str(e))
        return response.HttpResponseRedirect(reverse_lazy('indexHistoriaC'))