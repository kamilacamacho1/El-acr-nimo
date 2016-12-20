from lgm.apps.home.models import *
from django import forms
from django.contrib.auth.models import User


class Login_form(forms.Form):
	usuario = forms.CharField(widget = forms.TextInput())
	clave   = forms.CharField(widget = forms.PasswordInput(render_value = False))

#class RegisterForm(forms.ModelForm):
class RegisterForm(forms.ModelForm):
	username		= forms.CharField(label="Nombre de Usuario" ,widget=forms.TextInput())
	email			= forms.EmailField(label="Correo Electronico",widget=forms.TextInput())
	password_one	= forms.CharField(label="Password",widget=forms.PasswordInput(render_value=False))
	password_two	= forms.CharField(label="Confirmar password",widget=forms.PasswordInput(render_value=False))
	fecha_nacimiento = forms.DateField(widget=forms.TextInput(attrs={'id':'datepicker'}))
	class Meta:
		model = Persona
		exclude = ['foto','enfermedad','user']

	def clean_username(self):
		username = self.cleaned_data['username']
		try:
			u = User.objects.get(username=username)
		except User.DoesNotExist:
			return username
		raise forms.ValidationError('Nombre de usuario ya existe')

	def clean_email(self):
		email = self.cleaned_data['email']
		try:
			u = User.objects.get(email=email)
		except User.DoesNotExist:
			return email
		raise forms.ValidationError('Email ya registrado')

	def clean_password_two(self):
		password_one = self.cleaned_data['password_one']
		password_two = self.cleaned_data['password_two']
		if password_one == password_two:
			pass
		else:
			raise forms.ValidationError('Password no coinciden')

class contact_form(forms.Form):
	correo = forms.EmailField(widget = forms.TextInput())
	asunto = forms.CharField(widget = forms.TextInput())
	comentario = forms.CharField(widget = forms.Textarea())

class Tipo_Lugar_Form(forms.ModelForm):
	class Meta:
		model = Tipo_Lugar

class UbicacionForm(forms.ModelForm):
	tipo_lugar = forms.ModelChoiceField(queryset=Tipo_Lugar.objects.all(), empty_label="seleccione tipo lugar")
	class Meta:
		model = Ubicacion

class ValoracionForm(forms.ModelForm):
	class Meta:
		model = Valoracion 
		exclude = ['persona']


class seleccionar_enfermedades_form(forms.ModelForm):
	class Meta:
		model = Persona
		exclude = ['genero','fecha_nacimiento','user']

class DatoForm(forms.ModelForm):
	#nombre  		 = forms.CharField(label="Nombre de Usuario" ,widget=forms.TextInput())
	#apellido		 = forms.EmailField(label="Correo Electronico",widget=forms.TextInput())
	fecha_nacimiento = forms.DateField(widget=forms.TextInput(attrs={'id':'datepicker'}))
	class Meta:
		model = Persona
		exclude = ['genero','user']#,'fecha_nacimiento']

class user_form(forms.ModelForm):
	class Meta:
		model = User
		fields = ['first_name','last_name','username', 'email', ]
		exclude = '__all__'
		

	

	
	
	
	
	
		
