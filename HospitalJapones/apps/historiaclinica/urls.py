from django.urls import path
from .views import IndexHistoriaClinica, CreateHistoriaClinica

urlpatterns = [
    path('index', IndexHistoriaClinica.as_view(), name="indexHistoriaC"),
    path('create', CreateHistoriaClinica.as_view(), name="createhistoriaclinica" )
]