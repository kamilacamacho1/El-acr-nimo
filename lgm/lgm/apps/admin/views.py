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



def enfermedad_producto_view(request):
	info = ""
	form = Producto_Enfermedad_form()
	try:
		lista = Producto_Enfermedad.objects.all()
	except:
		lista=[] 
		print "no se pudo mostrar la lista"
	
	if request.method == "POST":
		formulario = Producto_Enfermedad_form(request.POST, request.FILES)
		if formulario.is_valid():
			add = formulario.save(commit = False)
			add.save()
			info = "Guardado Satisfactoriamente"
			return HttpResponseRedirect ('/enfermedad_producto/')
	else:
		form = Producto_Enfermedad_form()
	return render(request,'admin/enf_prod.html',locals() ) 

def single_producto_view(request, id_prod):
	prod = Producto.objects.get(id = id_prod) 
	ctx = {'producto':prod}
	return render_to_response('admin/single_producto.html',ctx,context_instance = RequestContext(request))

def productos_view (request, pagina):
	lista_prod = Producto.objects.filter()
	paginator  = Paginator(lista_prod,3)
	try:
		page = int(pagina)
	except:
		page = 1
	try:
		productos = paginator.page(page)
	except (EmptyPage,InvalidPage):
		productos = paginator.page(paginator.num_pages)

	ctx = {'productos':productos}
	return render_to_response('admin/productos.html', ctx, context_instance = RequestContext(request) )

def add_producto_view (request):
	info = "inicializando"
	if request.method == "POST":
		formulario = add_producto_form(request.POST, request.FILES)
		if formulario.is_valid():
			add = formulario.save(commit = False)
			
			add.save()
			formulario.save_m2m()
			info = "Guardado Satisfactoriamente"
			return HttpResponseRedirect ('/producto/%s' %add.id)
	else:
		formulario = add_producto_form()
	ctx = {'form':formulario, 'informacion':info}
	return render_to_response('admin/add_producto.html',ctx,context_instance = RequestContext(request))


def edit_producto_view(request,id_prod):
	info = ""
	producto = Producto.objects.get(pk = id_prod)
	if request.method == "POST":
		formulario = add_producto_form(request.POST,request.FILES,instance=producto)
		if formulario.is_valid():
			edit_prod = formulario.save(commit= False)
			formulario.save_m2m()
			
			edit_prod.save()
			info = "Guardado satisfactoriamente"
			return HttpResponseRedirect('/producto/%s'% edit_prod.id)
	else:
		formulario = add_producto_form(instance = producto)
	ctx = {'form':formulario, 'informacion':info}
	return render_to_response('admin/edit_producto.html',ctx,context_instance = RequestContext(request))
	

def del_producto_view (request, id_prod):
	info = "inicializando"
	try:
		prod = Producto.objects.get(pk = id_prod)
		prod.delete()
		info = "Producto Eliminada Correctamente"
		return HttpResponseRedirect('/productos/page/1')
	except:
		info = "Producto no se puede Eliminar"
		return HttpResponseRedirect('/productos/page/1')
		
def add_tipo_productos_view (request):
	try:
		tipos = Tipo_Producto.objects.all()
	except:
		pass
	if request.method == "POST":
		formulario = add_tipo_producto_form(request.POST)
		if formulario.is_valid():
			add = formulario.save(commit = False)
			add.save()
			return HttpResponseRedirect ('/add/tipo_productos/')
	else:
		formulario = add_tipo_producto_form()
	ctx = {'form':formulario, 'tipos':tipos}
	return render_to_response('admin/add_tipo_producto.html',ctx,context_instance = RequestContext(request))


def del_tipo_producto_view (request, id_prod):
	info = "inicializando"
	try:
		prod = Tipo_Producto.objects.get(pk = id_prod)
		prod.delete()
		info = " Tipo de Producto Eliminada Correctamente"
		return HttpResponseRedirect('/productos/page/1')
	except:
		info = "El Tipo de Producto no se puede Eliminar"
		return HttpResponseRedirect('/productos/page/1')





