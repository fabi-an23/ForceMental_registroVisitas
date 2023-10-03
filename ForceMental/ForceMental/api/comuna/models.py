from django.db import models
from api.cliente.models import Cliente

class Comuna(models.Model):
    id_comuna = models.AutoField(primary_key=True)
    nombre_comuna = models.CharField(max_length=255)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, db_column='cliente_id_cliente')

    class Meta:
        db_table = 'comuna'