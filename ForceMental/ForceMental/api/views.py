# Create your views here.
# En views.py de la aplicación correspondiente
from rest_framework import generics
from api.cliente.models import Cliente
from api.cliente.serializers import ClienteSerializer
from api.visita.models import Visita
from api.visita.serializers import VisitaSerializer
from api.region.models import Region
from api.provincia.models import Provincia
from api.comuna.models import Comuna
from api.region.serializers import RegionSerializer
from api.provincia.serializers import ProvinciaSerializer
from api.comuna.serializers import ComunaSerializer


class ClienteListView(generics.ListCreateAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
class ClienteDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    
class VisitaListView(generics.ListCreateAPIView):
    queryset = Visita.objects.all()
    serializer_class = VisitaSerializer

class VisitaDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Visita.objects.all()
    serializer_class = VisitaSerializer
    
class RegionListCreateView(generics.ListCreateAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer
    
class RegionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer
    
class ProvinciaListCreateView(generics.ListCreateAPIView):
    queryset = Provincia.objects.all()
    serializer_class = ProvinciaSerializer
    
class ProvinciaDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Provincia.objects.all()
    serializer_class = ProvinciaSerializer
    
class ComunaListCreateView(generics.ListCreateAPIView):
    queryset = Comuna.objects.all()
    serializer_class = ComunaSerializer

class ComunaDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comuna.objects.all()
    serializer_class = ComunaSerializer
