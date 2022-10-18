from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Fenomeno(models.Model):

    def _str_(self):

        return f"Nombre: {self.nombre} ------ Fecha: {self.fecha}"

    nombre = models.CharField(max_length=60)
    fecha = models.DateField()


class Acercademi(models.Model):
    info = models.CharField(max_length=60)


class Miembros(models.Model):
    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)
    email = models.EmailField(max_length=60)
    edad = models.IntegerField()


class Blog(models.Model):
    tuexperiencia = models.CharField(max_length=60)


class Avatar(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="avatares", null=True, blank=True)
