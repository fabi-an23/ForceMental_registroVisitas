# En models.py de la aplicación correspondiente
from django.db import models
from api.cliente.models import Cliente

class Visita(models.Model):
    id_visita = models.AutoField(primary_key=True)
    
    TIPO_VISITA_CHOICES = [
        ('F', 'Visita en Frío'),
        ('A', 'Visita Agendada'),
        ('S', 'Sin Tipo de Visita'),
    ]
    
    ESTADO_VISITA_CHOICES = [
        ('A', 'Aprobado'),
        ('R', 'Rechazado'),
        ('P', 'Pendiente'),
    ]
    
    tipo_visita = models.CharField(max_length=1, choices=TIPO_VISITA_CHOICES, default='F')
    estado_visita = models.CharField(max_length=1, choices=ESTADO_VISITA_CHOICES, default='P')
    
    cliente_id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha = models.DateField(null=True)
    hora = models.TimeField(null=True)
    lugar = models.CharField(max_length=255, blank=True)
    geolocalizacion = models.CharField(max_length=100, blank=True)
    
    def __str__(self):
        return f"Visita a {self.cliente.nombre} {self.cliente.apellido}"

