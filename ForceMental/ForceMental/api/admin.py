from django.contrib import admin

from django.contrib import admin
from api.cliente.models import Cliente
from api.visita.models import Visita

admin.site.register(Cliente)
admin.site.register(Visita)


