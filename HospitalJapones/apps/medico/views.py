from django.http import request
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.urls.base import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import login, logout

from django.views.generic import CreateView,ListView
from django.views.generic.edit import FormView
from .forms import FormularioLogin, FormCreateMedico
from .models import Medico


class CreateMedico(CreateView):
    model = Medico
    form_class = FormCreateMedico
    template_name = 'createMedico.html'

class IndexMedico(ListView):
    model = Medico
    template_name = 'indexMedico.html'

class Login(FormView):
    template_name = 'login.html'
    form_class = FormularioLogin
    success_url = reverse_lazy('indexHistoriaC')

    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self,request,*args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(Login,self).dispatch(request,*args, **kwargs)

    def form_valid(self,form):
        login(self.request,form.get_user())
        return super(Login,self).form_valid(form)

def logoutUsuario(request):
    logout(request)
    return HttpResponseRedirect('/accounts/login')