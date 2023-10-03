from django.db import models
from api.comuna.models import Comuna  # Importa el modelo de Comuna

class Provincia(models.Model):
    id_provincia = models.AutoField(primary_key=True)
    nombre_provincia = models.CharField(max_length=255)
    comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE, db_column='comuna_id_comuna', related_name='provincias')



    class Meta:
        db_table = 'provincia'
