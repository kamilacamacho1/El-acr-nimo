from django.shortcuts import render_to_response, render
from django.template import RequestContext
from lgm.apps.home.forms import *
from lgm.apps.home.models import *
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.utils import simplejson
from django.core.mail import EmailMultiAlternatives
from django.utils.timesince import timesince


def grafica_view(request):
	masamuscular = 0
	peso = 0
	grasa_viceral = 0	
	grasa_corporal = 0
	agua = 0
	masa_osea = 0
	edad_metabolica = 0
	bmr = 0
	info_enviado = True
	if request.user.is_authenticated(): #verifica si el ususario ya estas authentificado  o logueado
		if request.method == "POST":
			form = ValoracionForm(request.POST)
			if formulario.is_valid():


				masamuscular    = Valoracion.objects.filter(persona__user = request.user).count()			
				peso            = Valoracion.objects.filter(persona__user = request.user).count()
				grasa_viceral   = Valoracion.objects.filter(persona__user = request.user).count()
				grasa_corporal  = Valoracion.objects.filter(persona__user = request.user).count()
				agua            = Valoracion.objects.filter(persona__user = request.user).count()
				masa_osea       = Valoracion.objects.filter(persona__user = request.user).count()
				edad_metabolica = Valoracion.objects.filter(persona__user = request.user).count()
				bmr             = Valoracion.objects.filter(persona__user = request.user).count()
				info = "Valoracion Guardada"
				return HttpResponseRedirect('/grafica/')
			else:
				info= "Fallo"
		else:
			listaValoraciones = Valoracion.objects.filter(persona__user = request.user)		
			ctx = {'lista':listaValoraciones , 'masamuscular':masamuscular,'peso':peso,'grasa_viceral':grasa_viceral,'grasa_corporal':grasa_corporal,'agua':agua,'masa_osea':masa_osea,'edad_metabolica':edad_metabolica,'bmr':bmr,'info_enviado':info_enviado}
			return render_to_response('reportes/grafica.html', ctx, context_instance = RequestContext(request)) 
	else:
		return HttpResponseRedirect('/grafica/')
def reporte_view(request):

	masamuscular = 0
	peso = 0
	grasa_viceral = 0	
	grasa_corporal = 0
	agua = 0
	masa_osea = 0
	edad_metabolica = 0
	bmr = 0
	info_enviado = True
	if request.user.is_authenticated(): #verifica si el ususario ya estas authentificado  o logueado
		if request.method == "POST":
			form = ValoracionForm(request.POST)
			if formulario.is_valid():


				masamuscular    = Valoracion.objects.filter(persona__user = request.user).count()			
				peso            = Valoracion.objects.filter(persona__user = request.user).count()
				grasa_viceral   = Valoracion.objects.filter(persona__user = request.user).count()
				grasa_corporal  = Valoracion.objects.filter(persona__user = request.user).count()
				agua            = Valoracion.objects.filter(persona__user = request.user).count()
				masa_osea       = Valoracion.objects.filter(persona__user = request.user).count()
				edad_metabolica = Valoracion.objects.filter(persona__user = request.user).count()
				bmr             = Valoracion.objects.filter(persona__user = request.user).count()
				info = "Valoracion Guardada"
				return HttpResponseRedirect('reporte')
			else:
				info= "Fallo"
		else:
			listaValoraciones = Valoracion.objects.filter(persona__user = request.user)		
			ctx = {'lista':listaValoraciones , 'masamuscular':masamuscular,'peso':peso,'grasa_viceral':grasa_viceral,'grasa_corporal':grasa_corporal,'agua':agua,'masa_osea':masa_osea,'edad_metabolica':edad_metabolica,'bmr':bmr,'info_enviado':info_enviado}
			return render_to_response('reportes/reporte.html', ctx, context_instance = RequestContext(request)) 
	else:
		return HttpResponseRedirect('/reporte/')

		
def tanita_view (request):
	form = ValoracionForm()
	usu = request.user.id
	p = Persona.objects.get(user_id = usu)
	if request.method == "POST":
		form = ValoracionForm(request.POST)
		if form.is_valid():
			masamuscular    = form.cleaned_data['masamuscular']
			peso            = form.cleaned_data['peso']
			grasa_viceral   = form.cleaned_data['grasa_viceral']
			grasa_corporal  = form.cleaned_data['grasa_corporal']
			agua            = form.cleaned_data['agua']
			masa_osea       = form.cleaned_data['masa_osea']
			edad_metabolica = form.cleaned_data['edad_metabolica']
			bmr             = form.cleaned_data['bmr']
			valoracion = Valoracion.objects.create(
				masamuscular  = masamuscular,
				peso  = peso,
				grasa_viceral  = grasa_viceral,
				grasa_corporal = grasa_corporal,
				agua  = agua,
				masa_osea  = masa_osea,
				edad_metabolica  = edad_metabolica,
				bmr  = bmr,
				persona = p
				)
			return HttpResponseRedirect('/reporte/')
	else:
		form = ValoracionForm()
	ctx = {'form':form}
	return render_to_response('reportes/tanita.html',ctx,context_instance = RequestContext(request))

	
def grasa_view(request):

	grasa_corporal = 0

	info_enviado = True
	if request.user.is_authenticated(): #verifica si el ususario ya estas authentificado  o logueado
		if request.method == "POST":
			form = ValoracionForm(request.POST)
			if formulario.is_valid():


				grasa_corporal  = Valoracion.objects.filter(persona__user = request.user).count()
				return HttpResponseRedirect('/grasa/')
			else:
				info= "Fallo"
		else:
			listaValoraciones = Valoracion.objects.filter(persona__user = request.user)		
			ctx = {'lista':listaValoraciones ,'grasa_corporal':grasa_corporal,'info_enviado':info_enviado}
			return render_to_response('reportes/grasa.html', ctx, context_instance = RequestContext(request)) 
	else:
		return HttpResponseRedirect('/grasa/')


def osea_view(request):

	masa_osea = 0

	info_enviado = True
	if request.user.is_authenticated(): #verifica si el ususario ya estas authentificado  o logueado
		if request.method == "POST":
			form = ValoracionForm(request.POST)
			if formulario.is_valid():


				masa_osea  = Valoracion.objects.filter(persona__user = request.user).count()
				return HttpResponseRedirect('/osea/')
			else:
				info= "Fallo"
		else:
			listaValoraciones = Valoracion.objects.filter(persona__user = request.user)		
			ctx = {'lista':listaValoraciones ,'masa_osea':masa_osea,' info_enviado':info_enviado}
			return render_to_response('reportes/osea.html', ctx, context_instance = RequestContext(request)) 
	else:
		return HttpResponseRedirect('/osea/')

def viceral_view(request):

	agua = 0

	info_enviado = True
	if request.user.is_authenticated(): #verifica si el ususario ya estas authentificado  o logueado
		if request.method == "POST":
			form = ValoracionForm(request.POST)
			if formulario.is_valid():


				agua  = Valoracion.objects.filter(persona__user = request.user).count()
				return HttpResponseRedirect('/viceral/')
			else:
				info= "Fallo"
		else:
			listaValoraciones = Valoracion.objects.filter(persona__user = request.user)		
			ctx = {'lista':listaValoraciones ,'agua':agua,' info_enviado':info_enviado}
			return render_to_response('reportes/viceral.html', ctx, context_instance = RequestContext(request)) 
	else:
		return HttpResponseRedirect('/viceral/')


# Create your views here.
