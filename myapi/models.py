from django.db import models

class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    correo = models.CharField(max_length=100, unique=True)
    contrasena = models.CharField(max_length=100)

class InicioSesion(models.Model):
    id = models.AutoField(primary_key=True)
    correo = models.CharField(max_length=100, unique=True)
    contrasena = models.CharField(max_length=100)

class Sesion(models.Model):
    id = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    token = models.CharField(max_length=100, unique=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

class AlimentoMascota(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    tipo = models.CharField(max_length=20)

class AlimentoPerro(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    marca = models.CharField(max_length=50, choices=[('Marca1', 'Marca1'), ('Marca2', 'Marca2'), ('Marca3', 'Marca3'), ('Marca4', 'Marca4')])
    descripcion = models.CharField(max_length=50)
    precio = models.IntegerField()
    imagenURL = models.CharField(max_length=150)
    cantidad = models.IntegerField()

class AlimentoGato(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField( max_length=50)
    marca = models.CharField(max_length=50, choices=[('Marca1', 'Marca1'), ('Marca2', 'Marca2'), ('Marca3', 'Marca3'), ('Marca4', 'Marca4')])
    descripcion = models.CharField(max_length=50)
    precio = models.IntegerField()
    imagenURL = models.CharField(max_length=150)
    cantidad = models.IntegerField()

