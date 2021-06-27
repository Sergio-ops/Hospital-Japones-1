from django.urls import path
from .views import CreateMedico, IndexMedico

urlpatterns = [
    path('add',CreateMedico.as_view(),name='CrearMedico'),
    path('index',IndexMedico.as_view(),name='IndexMedico')
]