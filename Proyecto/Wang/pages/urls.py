from django.conf.urls import url
from . import views

urlpatterns = [
    #url(r'^$', views.index, name='index')
    url(r'^consulta$', views.expresion, name='expresion'),
    url(r'([^/]*)', views.index, name='index')
]