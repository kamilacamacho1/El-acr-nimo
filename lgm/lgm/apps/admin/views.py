from django.shortcuts import render_to_response, render
from django.template import RequestContext
from lgm.apps.home.forms import *
from lgm.apps.admin.forms import *
from lgm.apps.home.models import *
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, InvalidPage

def enfermedades_view (request, pagina):
	lista_prod = Enfermedad.objects.filter()
	paginator  = Paginator(lista_prod,3)
	try:
		page = int(pagina)
	except:
		page = 1
	try:
		enfermedades = paginator.page(page)
	except (EmptyPage,InvalidPage):
		enfermedades = paginator.page(paginator.num_pages)

	ctx = {'enfermedades':enfermedades}
	return render_to_response('admin/enfermedades.html', ctx, context_instance = RequestContext(request) )
	#return render ('home/enfermedades.html', locals(),request)
def single_enfermedad_view(request, id_prod):
	prod = Enfermedad.objects.get(id = id_prod) 
	ctx = {'enfermedad':prod}
	return render_to_response('admin/single_enfermedad.html',ctx,context_instance = RequestContext(request))


def add_enfermedad_view (request):
	info = "inicializando"
	if request.method == "POST":
		formulario = add_enfermedad_form(request.POST, request.FILES)
		if formulario.is_valid():
			add = formulario.save(commit = False)
			
			add.save()
			formulario.save_m2m()
			info = "Guardado Satisfactoriamente"
			return HttpResponseRedirect ('/enfermedad/%s' %add.id)
	else:
		formulario = add_enfermedad_form()
	ctx = {'form':formulario, 'informacion':info}
	return render_to_response('admin/add_enfermedad.html',ctx,context_instance = RequestContext(request))


def edit_enfermedad_view(request,id_prod):
	info = ""
	enfermedad = Enfermedad.objects.get(pk = id_prod)
	if request.method == "POST":
		formulario = add_enfermedad_form(request.POST,request.FILES,instance=enfermedad)
		if formulario.is_valid():
			edit_prod = formulario.save(commit= False)
			formulario.save_m2m()
			
			edit_prod.save()
			info = "Guardado satisfactoriamente"
			return HttpResponseRedirect('/enfermedad/%s'% edit_prod.id)
	else:
		formulario = add_enfermedad_form(instance = enfermedad)
	ctx = {'form':formulario, 'informacion':info}
	return render_to_response('admin/edit_enfermedad.html',ctx,context_instance = RequestContext(request))
	


def del_enfermedad_view (request, id_prod):
	info = "inicializando"
	try:
		prod = Enfermedad.objects.get(pk = id_prod)
		prod.delete()
		info = "Enfermedad Eliminada Correctamente"
		return HttpResponseRedirect('/enfermedades/page/1')
	except:
		info = "Enfermedad no se puede Eliminar"
		return HttpResponseRedirect('/enfermedades/page/1')
# Create your views here.


def add_tipo_enfermedades_view (request):
	try:
		tipos = Tipo_Enfermedad.objects.all()
	except:
		pass
	if request.method == "POST":
		formulario = add_tipo_enfermedad_form(request.POST)
		if formulario.is_valid():
			add = formulario.save(commit = False)
			add.save()
			return HttpResponseRedirect ('/add/tipo_enfermedades/')
	else:
		formulario = add_tipo_enfermedad_form ()
	ctx = {'form':formulario, 'tipos':tipos}
	return render_to_response('admin/add_tipo_enfermedad.html',ctx,context_instance = RequestContext(request))


def del_tipo_enfermedad_view (request, id_prod):
	info = "inicializando"
	try:
		prod = Tipo_Enfermedad.objects.get(pk = id_prod)
		prod.delete()
		info = " Tipo de Enfermedad Eliminada Correctamente"
		return HttpResponseRedirect('/enfermedades/page/1')
	except:
		info = "El Tipo de Enfermedad no se puede Eliminar"
		return HttpResponseRedirect('/enfermedades/page/1')