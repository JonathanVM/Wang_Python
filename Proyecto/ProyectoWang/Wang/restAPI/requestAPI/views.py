from django.shortcuts import render
from rest_framework import viewsets
from .models import Pruebas

import sys
sys.path.insert(0, '..\ANTLR\src')
from .serializers import PruebasSerializer

class PruebasView(viewsets.ModelViewSet):
    queryset = Pruebas.objects.all()
    serializer_class = PruebasSerializer

# Create your views here.
