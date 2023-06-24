from rest_framework import viewsets
from .serializers import UsuarioSerializer, SesionSerializer, AlimentoMascotaSerializer, AlimentoPerroSerializer, AlimentoGatoSerializer
from .models import Usuario, Sesion, AlimentoMascota, AlimentoPerro, AlimentoGato

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class SesionViewSet(viewsets.ModelViewSet):
    queryset = Sesion.objects.all()
    serializer_class = SesionSerializer

class AlimentoMascotaViewSet(viewsets.ModelViewSet):
    queryset = AlimentoMascota.objects.all()
    serializer_class = AlimentoMascotaSerializer

class AlimentoPerroViewSet(viewsets.ModelViewSet):
    queryset = AlimentoPerro.objects.all()
    serializer_class = AlimentoPerroSerializer

class AlimentoGatoViewSet(viewsets.ModelViewSet):
    queryset = AlimentoGato.objects.all()
    serializer_class = AlimentoGatoSerializer