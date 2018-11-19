from rest_framework import serializers
from .models import Pruebas

import sys
sys.path.insert(0, '..\ANTLR\src')

from visitor import *
from wang import *

from deduction import *
from deductionTree import *

class PruebasSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pruebas
        fields = ('id','url','expresion','respuesta')
        read_only_fields = ('respuesta',)
        
    def create(self, data):
        print('Llega')
        print(f">>>probador {data}")
        expre = data['expresion']
        print(f">>>expresion {expre}")
        result = deductionParser(expre)
        for i in range(len(result)):
            arbolDeduction = DeductionTree()
            salidaArbol = arbolDeduction.buildTree(result[i])
            print(salidaArbol)
            data['respuesta'] = salidaArbol
        print(f"Posicion 0: {result[0]}")
        return super().create(data)
        
    