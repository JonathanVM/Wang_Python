'''
autores:
    Delia Hernandez Ruiz
    Jonathan Vasquez Mora
    Erick Hernandez Camacho
'''

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'([^/]*)', views.index, name='index')
]