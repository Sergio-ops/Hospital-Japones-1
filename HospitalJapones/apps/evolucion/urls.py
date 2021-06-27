from django.urls import path
from .views import EvolucionListFilterbyHC, EvolucionDetailCreate, EvolucionUpdate, change_status, DetalleEvolucion

urlpatterns = [
    path('index/<int:fk>', EvolucionListFilterbyHC.as_view(),name='EvolucionFilter'),
    path('create/<int:id>', EvolucionDetailCreate.as_view(),name='EvolucionCreate'),
    path('update/<int:pk>', EvolucionUpdate.as_view(),name='EvolucionUpdate'),
    path('anular', change_status,name='EvolucionChangeSatus'),
    path('detalle/<int:pk>', DetalleEvolucion.as_view(),name='EvolucionDetail'),
]