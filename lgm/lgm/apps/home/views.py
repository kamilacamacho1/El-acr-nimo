from django.shortcuts import render_to_response, render
from django.template import RequestContext
from lgm.apps.home.forms import *
from django.http import HttpResponseRedirect

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


# Create your views here.