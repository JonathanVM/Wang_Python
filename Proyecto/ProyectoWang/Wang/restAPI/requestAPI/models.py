from django.db import models

# Create your models here.

class Pruebas(models.Model):
    expresion = models.CharField(max_length=100)
    respuesta = models.CharField(max_length=1500)
    def __str__(self):
        return self.expresion