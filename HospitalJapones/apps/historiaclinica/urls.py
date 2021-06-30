from django.urls import path
from .views import IndexHistoriaClinica, CreateHistoriaClinica, UpdateHistoriaClinica

urlpatterns = [
    path('index', IndexHistoriaClinica.as_view(), name="indexHistoriaC"),
    path('create', CreateHistoriaClinica.as_view(), name="createhistoriaclinica" ),
    path('update/<int:pk>', UpdateHistoriaClinica.as_view(), name="updatehistoriaclinica" ),
]