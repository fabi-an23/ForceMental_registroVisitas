from rest_framework import serializers
from .models import Provincia
from api.comuna.models import Comuna
from api.comuna.serializers import ComunaSerializer



class ProvinciaSerializer(serializers.ModelSerializer):
    comunas = serializers.PrimaryKeyRelatedField(
        many=True, 
        read_only=True, 
        source='comuna_set'  # Esto mostrará la lista de IDs de las comunas asociadas
    )
    comuna = serializers.PrimaryKeyRelatedField(queryset=Comuna.objects.all(), write_only=True)

    class Meta:
        model = Provincia
        fields = ['id_provincia', 'nombre_provincia', 'comunas', 'comuna']

    def create(self, validated_data):
        # Se elimina 'comuna' del diccionario validated_data porque es un campo virtual
        comuna_data = validated_data.pop('comuna', None)
        provincia = Provincia.objects.create(**validated_data)

        if comuna_data:
            provincia.comuna = comuna_data
            provincia.save()

        return provincia