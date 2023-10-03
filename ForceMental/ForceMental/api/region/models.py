from django.db import models
from api.provincia.models import Provincia  # Importa el modelo de Provincia

class Region(models.Model):
    id_region = models.AutoField(primary_key=True)
    nombre_region = models.CharField(max_length=50)
    provincia = models.ForeignKey(Provincia, on_delete=models.CASCADE, db_column='provincia_id_provincia', related_name='regiones')


    class Meta:
        db_table = 'region'
