# En serializers.py de la aplicación correspondiente
from rest_framework import serializers
from .models import Visita
from api.cliente.models import Cliente
from api.cliente.serializers import ClienteSerializer

class VisitaSerializer(serializers.ModelSerializer):
    cliente = ClienteSerializer(source='cliente_id_cliente', read_only=True)

    class Meta:
        model = Visita
        fields = ['id_visita', 'tipo_visita', 'estado_visita', 'fecha', 'hora', 'lugar', 'geolocalizacion', 'cliente']