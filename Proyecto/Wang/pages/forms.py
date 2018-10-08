from django import forms

class ProbarForm(forms.Form):
    cadena = forms.CharField(max_length=200)