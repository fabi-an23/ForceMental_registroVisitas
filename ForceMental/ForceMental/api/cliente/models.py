from django.db import models

# Create your models here.
# En models.py de la aplicación correspondiente

class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    correo_electronico = models.EmailField()
    direccion = models.CharField(max_length=255)
    estado_cliente = models.CharField(max_length=20, choices=[('A', 'Aprobado'), ('R', 'Rechazado')])

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
