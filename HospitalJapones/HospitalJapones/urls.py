"""HospitalJapones URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from apps.medico.views import Login, logoutUsuario

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/',Login.as_view(),name='login'),
    path('logout/',logoutUsuario,name='logout'),
    path('medico/', include('apps.medico.urls')),
    path('paciente/', include('apps.paciente.urls')),
    path('historia/', include('apps.historiaclinica.urls')),
    path('evolucion/', include('apps.evolucion.urls')),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
