from django.shortcuts import render
from rest_framework import viewsets
from .models import Pruebas
from .serializers import PruebasSerializer

class PruebasView(viewsets.ModelViewSet):
    queryset = Pruebas.objects.all()
    serializer_class = PruebasSerializer

# Create your views here.
