from rest_framework import serializers
from .models import Pruebas
from Proyecto.ProyectoWang.ANTLR.src.visitor import *
#from deduction import *
#from visitor import WangPrintVisitor

class PruebasSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pruebas
        fields = ('id','url','idExpresion','expresion')
        
    def create(self, data):
        print(f">>>probador {data}")
        expre = data['expresion']
        print(f">>>expresion {expre}")
        result = WangPrintVisitor()
        return super().create(data) 
        
    