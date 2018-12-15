'''
autores:
    Delia Hernandez Ruiz
    Jonathan Vasquez Mora
    Erick Hernandez Camacho
'''

from django.urls import path
from .views import PruebasAPIView, PruebasAPIDetail, PruebasAPIAllView

urlpatterns = [
    path('', PruebasAPIView.as_view()),
    path('<int:pk>/',PruebasAPIDetail.as_view()),
    path('all/',PruebasAPIAllView.as_view()),
]