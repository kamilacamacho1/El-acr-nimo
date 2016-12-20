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
from datetime import date 

def nutricion_view (request):
#	p = Persona.objects.get(id = request.user.id)
#	lista = Producto_Enfermedad.objects.filter(persona__enfermedad = p)
	return render_to_response('home/nutricion.html', context_instance = RequestContext(request))

def dato_view (request):
	#form = DatoForm()
	#usu = request.user.id
	usu = User.objects.get(pk =request.user.id) 
	p = Persona.objects.get(user = usu)
	if request.method == "POST":
		form = DatoForm(request.POST,instance= p)
		form_b = user_form(request.POST,instance= usu)
		if form.is_valid() and form_b.is_valid()  :
			d = form.save(commit = False)
			d.user = usu
			x = form.cleaned_data['fecha_nacimiento']
			d.fecha_nacimiento = x
			form.save_m2m()
			form_b.save()
			d.save() 
			return HttpResponseRedirect('/dato/')
	else:
		form = DatoForm(instance = p)
		form_b = user_form(instance = usu)

	ctx = {'form':form,'form_b':form_b}
	return render_to_response('home/dato.html',ctx,context_instance = RequestContext(request))


def seleccionar_enfermedades_view (request):
	usuario = Persona.objects.filter(user = request.user)
	if request.method == "POST":
		form = seleccionar_enfermedades_form(request.POST)
		if form.is_valid():
			seleccionada = form.save(commit = False)
			form.save_m2m()
			seleccionada.save()
			ctx = {'form':form, 'now':now}
			return render_to_response('home/seleccionar_enfermedades.html',ctx,context_instance=RequestContext(request))
	else:
		form = seleccionar_enfermedades_form()
	ctx = {'form':form}
	return render_to_response('home/seleccionar_enfermedades.html', ctx, context_instance = RequestContext(request))	



def valoraciones_view (request):
	p = User.objects.get(id = request.user.id)
	lista = Valoracion.objects.filter(persona__user = p)
	return render(request,'home/tabla.html',locals())


def register_view(request):
		form = RegisterForm()
		now = date.today()
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
			ctx = {'form':form, 'now':now}
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
lista[-1]
lista.ALGO ULTIMO ELEMENTO DE LA LISTA

'''


#graficas
def grafica_view(request):

	info_enviado = True
	if request.user.is_authenticated(): #verifica si el ususario ya estas authentificado
		listaValoraciones = Valoracion.objects.filter(persona__user = request.user)[:6]	
		ctx = {'lista':listaValoraciones ,'info_enviado':info_enviado}
		return render_to_response('home/grafica.html', ctx, context_instance = RequestContext(request)) 
	else:
		return HttpResponseRedirect('/grafica/')

def reporte_view(request):

	info_enviado = True
	if request.user.is_authenticated(): #verifica si el ususario ya estas authentificado
		listaValoraciones = Valoracion.objects.filter(persona__user = request.user)[:6]	
		ctx = {'lista':listaValoraciones ,'info_enviado':info_enviado}
		return render_to_response('home/reporte.html', ctx, context_instance = RequestContext(request)) 
	else:
		return HttpResponseRedirect('/reporte/')

		
def tanita_view (request):
	form = ValoracionForm()
	usu = request.user.id
	p = Persona.objects.get(user_id = usu)
	if request.method == "POST":
		form = ValoracionForm(request.POST)
		if form.is_valid():
			val = form.save(commit = False)
			val.persona = p
			val.save() 
			return HttpResponseRedirect('/valoraciones/')
	else:
		form = ValoracionForm()
	ctx = {'form':form}
	return render_to_response('home/tanita.html',ctx,context_instance = RequestContext(request))

	
def grasa_view(request):
	info_enviado = True
	if request.user.is_authenticated(): #verifica si el ususario ya estas authentificado
		listaValoraciones = Valoracion.objects.filter(persona__user = request.user)[:6]	
		ctx = {'lista':listaValoraciones ,'info_enviado':info_enviado}
		return render_to_response('home/grasa.html', ctx, context_instance = RequestContext(request)) 
	else:
		return HttpResponseRedirect('/grasa/')



def osea_view(request):
	info_enviado = True
	if request.user.is_authenticated(): #verifica si el ususario ya estas authentificado
		listaValoraciones = Valoracion.objects.filter(persona__user = request.user)[:6]	
		ctx = {'lista':listaValoraciones ,'info_enviado':info_enviado}
		return render_to_response('home/osea.html', ctx, context_instance = RequestContext(request)) 
	else:
		return HttpResponseRedirect('/osea/')


def viceral_view(request):

	info_enviado = True
	if request.user.is_authenticated(): #verifica si el ususario ya estas authentificado
		listaValoraciones = Valoracion.objects.filter(persona__user = request.user)[:6]	
		ctx = {'lista':listaValoraciones ,'info_enviado':info_enviado}
		return render_to_response('home/viceral.html', ctx, context_instance = RequestContext(request)) 
	else:
		return HttpResponseRedirect('/viceral')


#graficas





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


def ubicaciones_view(request):
	ubicaciones = Ubicacion.objects.all()
	lista = []
	for x in ubicaciones:
		ubicacion = str (x.lat+","+x.lng)
		lista.append(ubicacion)
	

	return render_to_response('home/ubicaciones.html', {'ubicaciones':lista, 'nombre': ubicaciones}, context_instance = RequestContext(request))


# Create your views here.
#administrador



#administrador