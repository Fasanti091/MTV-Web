from django.db import models

# Create your models here.

class Familiares(models.Model):
    nombre = models.CharField(max_length=40) 
    apellido = models.CharField(max_length=40)
    edad = models.IntegerField()