from rest_framework.views import APIView
from rest_framework.response import Response
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

class RegistroView(APIView):
    def post(self, request):
        # Extract data from the request, perform validation, and save the user
        serializer = UsuarioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User registered successfully"})
        return Response(serializer.errors, status=400)    
    