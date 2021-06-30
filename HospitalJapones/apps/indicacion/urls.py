from django.urls import path
from .views import CreateIndicacion

urlpatterns = [
    path('create/<int:pk>', CreateIndicacion.as_view(), name='createIndicacion'),
]