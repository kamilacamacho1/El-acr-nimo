from lgm.apps.home.models import *
from django import forms
from django.contrib.auth.models import User

class add_enfermedad_form(forms.ModelForm):
	class Meta:
		model 	= Enfermedad
		exclude = ['frecuencia']

class add_tipo_enfermedad_form(forms.ModelForm):
	class Meta:
		model 	= Tipo_Enfermedad
		

		