from lgm.apps.home.models import *
from django import forms

class add_Clase_form (forms.ModelForm):
	class Meta:
		model = Clase

