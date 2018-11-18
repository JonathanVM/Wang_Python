from django.db import models

# Create your models here.

class Pruebas(models.Model):
    expresion = models.CharField(max_length=100)
    #idExpresion = models.CharField(max_length=100)
    def __str__(self):
        return self.expresion