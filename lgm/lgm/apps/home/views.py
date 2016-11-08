from django.shortcuts import render_to_response, render
from django.template import RequestContext
from lgm.apps.home.forms import *
from lgm.apps.home.models import *
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User


def register_view(request):
	form = RegisterForm()
	if request.method == "POST":
		form = RegisterForm(request.POST)
		if form.is_valid():
			usuario = form.cleaned_data['username']
			email = form.cleaned_data['email']
			password_one = form.cleaned_data['password_one']
			password_two = form.cleaned_data['password_two']
			u = User.objects.create_user(username=usuario,email=email,password=password_one)
			u.save() # Guardar el objeto
			return render_to_response('home/thanks_register.html',context_instance=RequestContext(request))
		else:
			ctx = {'form':form}
			return render_to_response('home/register.html',ctx,context_instance = RequestContext(request))
	ctx = {'form':form}
	return render_to_response('home/register.html',ctx,context_instance = RequestContext(request))



def index_view (request):
	return render_to_response('home/index.html', context_instance = RequestContext(request))

def add_clase_view (request):
	info = "inicializado"
	if request.method == "POST":
		formulario = add_Clase_form(request.POST, request.FILES)
		if formulario.is_valid():
			add = formulario.save(commit = False)
			add.status = True
			add.save() # guarda la informacion
			formulario.save_m2m() # guarda las relaciones ManyToMany
			info = "Guardado Satisfactoriamente"
			return HttpResponseRedirect ('/') #('/Producto/%s' %add.id)
	else:
		formulario = add_Clase_form()
	ctx = {'form':formulario, 'informacion':info}
	return render_to_response('home/add_clase.html', ctx,context_instance = RequestContext(request))# Create your views here.



def login_view (request):
	mensage = ""
	if request.user.is_authenticated(): #verifica si el ususario ya estas authentificado  o logueado
		return HttpResponseRedirect('/')
	else: #si no fue POST entonces fue el metodo GET mostrara un formulario vacio
		if request.method == "POST":
			formulario = Login_form(request.POST)
			if formulario.is_valid():
				usu = formulario.cleaned_data['usuario']
				pas = formulario.cleaned_data['clave']
				usuario = authenticate(username = usu, password = pas)
				if usuario is not None and usuario.is_active:
					login(request, usuario)
					return HttpResponseRedirect('/')
				else:
					mensage = "usuario y/o clave incorrecta"
		formulario = Login_form()
		ctx = {'form':formulario, 'mensage':mensage}
		return render_to_response('home/login.html',ctx,context_instance = RequestContext(request))

def logout_view(request):
	logout(request)
	return HttpResponseRedirect('/')




def tanita_view (request):
	return render_to_response('home/tanita.html', context_instance = RequestContext(request))



