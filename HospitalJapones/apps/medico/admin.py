from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Medico

admin.site.register(Medico, UserAdmin)
