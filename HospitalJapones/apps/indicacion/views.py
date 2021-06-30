from django.shortcuts import get_object_or_404, render
from django.views.generic import CreateView, DetailView
from .models import Indicacion
from ..evolucion.models import Evolucion
from .forms import FormIndicacion

class CreateIndicacion(DetailView):
    model = Indicacion
    form_class = FormIndicacion
    template_name = 'indicacionapp/create.html'

    def get_object(self):
        id = self.kwargs.get("pk")
        return get_object_or_404(Evolucion, id_evolucionPK=id)