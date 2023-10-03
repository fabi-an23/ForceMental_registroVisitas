# En serializers.py de la aplicación correspondiente
from rest_framework import serializers
from api.cliente.models import Cliente
from api.comuna.serializers import ComunaSerializer

class ClienteSerializer(serializers.ModelSerializer):
    comuna = ComunaSerializer(source='comuna_set', many=True, read_only=True)  # Esto mostrará la información detallada de la comuna asociada al cliente
    
    class Meta:
        model = Cliente
        fields = '__all__'
