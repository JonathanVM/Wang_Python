'''
autores:
    Delia Hernandez Ruiz
    Jonathan Vasquez Mora
    Erick Hernandez Camacho
'''

from rest_framework import generics
from .models import Pruebas

import sys
sys.path.insert(0, '..\ANTLR\src')
from .serializers import PruebasSerializer

# Create your views here.

class PruebasAPIView(generics.ListCreateAPIView):
    queryset = Pruebas.objects.all()
    serializer_class = PruebasSerializer
    
class PruebasAPIDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pruebas.objects.all()
    serializer_class = PruebasSerializer
    
class PruebasAPIAllView(generics.ListAPIView):
    queryset = Pruebas.objects.all()
    serializer_class = PruebasSerializer


