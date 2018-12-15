'''
autores:
    Delia Hernandez Ruiz
    Jonathan Vasquez Mora
    Erick Hernandez Camacho
'''


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
            print(f"Position 0: {result[0]}")
            for i in range(len(result)):
                arbolDeduction = DeductionTree()
                salidaArbol = arbolDeduction.buildTree(result[i])
                data['respuesta'] = salidaArbol
        except (IndexError, SystemExit):
            data['respuesta'] = "Invalid Expression"
        return super().create(data)
        
    