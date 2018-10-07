
from django import forms

class ConsultaForm(forms.Form):
    ecuacion = forms.CharField(required=True)