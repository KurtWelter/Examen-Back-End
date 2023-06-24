from rest_framework import serializers

from .models import Usuario
from .models import Sesion
from .models import AlimentoMascota
from .models import AlimentoPerro
from .models import AlimentoGato

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'nombre', 'apellido', 'correo', 'contrasena']

class SesionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sesion
        fields = ['id', 'usuario', 'token', 'fecha_creacion']

class AlimentoMascotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlimentoMascota
        fields = ['id', 'nombre', 'tipo']

class AlimentoPerroSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlimentoPerro
        fields = ['id', 'alimento', 'marca', 'sabor']

class AlimentoGatoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlimentoGato
        fields = ['id', 'alimento', 'marca', 'sabor']