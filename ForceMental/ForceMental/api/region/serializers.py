from rest_framework import serializers
from .models import Region
from api.provincia.serializers import ProvinciaSerializer

class RegionSerializer(serializers.ModelSerializer):
    provincia = ProvinciaSerializer(read_only=True, source='provincia_set')  # Esto mostrará la información detallada de la provincia asociada

    class Meta:
        model = Region
        fields = ['id_region', 'nombre_region', 'provincia']
