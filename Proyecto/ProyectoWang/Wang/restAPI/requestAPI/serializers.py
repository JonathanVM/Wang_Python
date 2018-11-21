from rest_framework import serializers
from .models import Pruebas

import sys
sys.path.insert(0, '..\ANTLR\src')

from visitor import *
from wang import *

from deduction import *
from deductionTree import *

class PruebasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pruebas
        fields = ('id','expresion','respuesta')
        read_only_fields = ('respuesta',)
        
    def create(self, data):
        expre = data['expresion']
        try:
            result = deductionParser(expre)
            print(f"Posicion 0: {result[0]}")
            for i in range(len(result)):
                arbolDeduction = DeductionTree()
                salidaArbol = arbolDeduction.buildTree(result[i])
                print(salidaArbol)
                data['respuesta'] = salidaArbol
            return super().create(data)
        except IndexError:
            print('entro, expresion invalida')
            data['respuesta'] = "Expresión invalida"
            return super().create(data)
        except SystemExit:
            print('entro, expresion invalida')
            data['respuesta'] = "Expresión invalida"
            return super().create(data)
        
    