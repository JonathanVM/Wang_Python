from rest_framework import serializers
from .models import Pruebas

class PruebasSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pruebas
        fields = ('id','url','idExpresion','expresion')