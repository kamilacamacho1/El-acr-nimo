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

def nutricion_view (request):
	return render_to_response('home/nutricion.html', context_instance = RequestContext(request))

def register_view(request):
		form = RegisterForm()
		if request.method == "POST":
			form = RegisterForm(request.POST)
			if form.is_valid():
				usuario          = form.cleaned_data['username']
				genero           = form.cleaned_data['genero']
				fecha_nacimiento = form.cleaned_data['fecha_nacimiento']
				email            = form.cleaned_data['email']
				password_one     = form.cleaned_data['password_one']
				password_two     = form.cleaned_data['password_two']
				u = User.objects.create_user(username=usuario,email=email,password=password_one)
				u.save()
				p = Persona.objects.create(genero=genero,fecha_nacimiento=fecha_nacimiento, user = u)
			p.save() # Guardar el objeto
			return render_to_response('home/thanks_register.html',context_instance=RequestContext(request))
		else:
			ctx = {'form':form}
			return render_to_response('home/register.html',ctx,context_instance = RequestContext(request))
			ctx = {'form':form}
			return render_to_response('home/register.html',ctx,context_instance = RequestContext(request))



def index_view (request):
	return render_to_response('home/index.html', context_instance = RequestContext(request))


def about_view (request):
	return render_to_response('home/about.html', context_instance = RequestContext(request))	

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

'''
lista=[1,2,3,a,hola]
lista[4]
lista.ALGO ULTIMO ELEMENTO DE LA LISTA

'''


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
	return render_to_response('home/tanita.html',ctx,context_instance = RequestContext(request))


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
			listaValoraciones = Valoracion.objects.all()		
			ctx = {'lista':listaValoraciones , 'masamuscular':masamuscular,'peso':peso,'grasa_viceral':grasa_viceral,'grasa_corporal':grasa_corporal,'agua':agua,'masa_osea':masa_osea,'edad_metabolica':edad_metabolica,'bmr':bmr,'info_enviado':info_enviado}
			return render_to_response('home/reporte.html', ctx, context_instance = RequestContext(request)) 
	else:
		return HttpResponseRedirect('/reporte/')


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
			listaValoraciones = Valoracion.objects.all()		
			ctx = {'lista':listaValoraciones , 'masamuscular':masamuscular,'peso':peso,'grasa_viceral':grasa_viceral,'grasa_corporal':grasa_corporal,'agua':agua,'masa_osea':masa_osea,'edad_metabolica':edad_metabolica,'bmr':bmr,'info_enviado':info_enviado}
			return render_to_response('home/grafica.html', ctx, context_instance = RequestContext(request)) 
	else:
		return HttpResponseRedirect('/grafica/')


def contact_view (request):
	info_enviado = False #Definir  si se envio la informacion o no se envio
	email = ""
	title = ""
	text = ""
	if request.method == "POST": # evalua si el metodo fue POST
		formulario = contact_form(request.POST) #instancia del formulario con los datos ingresados
		if formulario.is_valid(): #evalua si el formulario es valido
			info_enviado = True #la informacion se envio correctamente
			email = formulario.cleaned_data['correo'] #copia el correo ingresado en email
			title = formulario.cleaned_data['asunto'] #copia el titulo ingresado en title
			text = formulario.cleaned_data['comentario'] #copia en texto ingresado en text

			''' Bloque configuracion de envio por GMAIL '''
			to_admin = 'sena954082@gmail.com'
			html_content = "Informacion recibida de %s <br> ---Mensaje--- <br> %s"%(email,text)
			msg = EmailMultiAlternatives('correo de contacto', html_content, 'from@server.com',[to_admin])
			msg.attach_alternative(html_content, 'text/html') #definimos el contenido como HTML
			msg.send() #enviamos el correo
			''' Fin del bloque '''

	else: #si no fue POST entonces fue el metodo GET mostrara un formulario vacio
		formulario = contact_form() #creacion del formulario vacio
	ctx = {'form':formulario, 'email' :email, "title":title, "text":text, "info_enviado":info_enviado}
	return render_to_response('home/contact.html',ctx,context_instance = RequestContext(request))	

def coords_save(request):
	if request.is_ajax():
		form = UbicacionForm(request.POST)
		if form.is_valid():
			form.save()
			ubicaciones = Ubicacion.objects.all().order_by('-fecha')

			data = '<ul id="ubicaciones">'
			for ubicacion in ubicaciones:
				data += '<li>%s %s - hace%s</li>' % (ubicacion.nombre, ubicacion.tipo_lugar, timesince(ubicacion.fecha))

			data += '</ul>'
			print "valid"	
			return HttpResponse(simplejson.dumps({'ok':True, 'msg':data}), mimetype='application/json')
		else:
			print "invalid"
			return HttpResponse(simplejson.dumps({'ok':False, 'msg': 'Debes llenar todos los campos'}), mimetype='application/json') 
	"""
	form = UbicacionForm()
	ubicaciones = Tipo_Lugar.objects.all()
	print "ubi "+ str(len(ubicaciones))

	return render_to_response('home/mapa.html', {'form':form, 'ubicaciones':ubicaciones}, context_instance = RequestContext(request))
"""
		


def mapa_view(request):
	ubicaciones = Ubicacion.objects.all()
	lista =[ ]
	for x in ubicaciones:
		ubicacion = str ( x.nombre ) 
		lista.append(ubicacion)
   


	form = UbicacionForm()
	#ubicaciones = Tipo_Lugar.objects.all()

	return render_to_response('home/mapa.html', {'form':form, 'ubicaciones':lista}, context_instance = RequestContext(request))


def mapa1_view(request):
	#ubicacion = ubicacion.objects.all()
	return render_to_response('home/mapa1.html', context_instance = RequestContext(request))
# Create your views here.
