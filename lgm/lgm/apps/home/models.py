from django.db import models
from django.contrib.auth.models import User

''' Enfermedades '''
class Tipo_Enfermedad(models.Model):
	nombre = models.CharField(max_length = 100)

	def __unicode__ (self):
		return self.nombre

	class Meta:
		verbose_name_plural = "Tipo_Enfemedad"


class Enfermedad(models.Model):
	nombre = models.CharField(max_length = 100)
	#codigo = models.CharField(max_length = 100)
	#origen = models.TextField(max_length = 500)
	#curso  = models.CharField(max_length = 100)
	frecuencia = models.CharField(max_length =100) #periocidad
	tipo = models.ForeignKey(Tipo_Enfermedad)

	def __unicode__ (self):
		return self.nombre

	class Meta:
		verbose_name_plural = "Enfermedad"
	
''' Fin Enfermedades '''
                               

class Producto(models.Model):
	def url(self, filename):
		ruta = "MultimediaData/Productos/%s/%s"%(self.nombre, str(filename))
		return rutams

	nombre      = models.CharField(max_length = 100)
	precio      = models.CharField(max_length = 100)
	descripcion = models.TextField(max_length=100)
	#stock       = models.IntegerField()
	imagen     = models.ImageField(upload_to = url, null = True, blank = True)


	def __unicode__ (self):
		return self.nombre

	class Meta:
		verbose_name_plural = "Producto"
	
RECOMENDADO = (
	('si','si'), 
	('no','no'), 
)

class Producto_Enfermedad(models.Model):
	pro       	= models.ForeignKey(Producto, unique = True)
	enf        	= models.ForeignKey(Enfermedad)#, unique = True)
	recomendable= models.CharField(max_length = 50, choices = RECOMENDADO )

	
	def __unicode__ (self):
		return self.pro.nombre + " "  + self.enf.nombre + " "  + self.recomendable

	class Meta:
		verbose_name_plural = "Producto_Enfermedad"

HORARIOS=(
	("Desayuno","Desayuno"),
	("Merienda","Merienda"),
	("Almuerzo","Almuerzo"),
	("Media Tarde","Media Tarde"),
	("Cena","Cena"),
	
	

)		
	
class Dieta(models.Model):
	clasificacion= models.CharField(max_length = 100)
	horario      = models.CharField(max_length = 100, choices = HORARIOS )
	suplementos  = models.TextField(max_length=100)
	porciones    = models.CharField(max_length=100)
	producto     = models.ManyToManyField(Producto, null= True, blank = True)

 	def __unicode__ (self):
		return self.clasificacion

	class Meta:
		verbose_name_plural = "Dieta"

GENEROS =(
	('Hombre','Hombre'),
	('Mujer','Mujer'),

)
	

class Persona (models.Model):
	def url(self, filename):
		ruta = "MultimediaData/User/%s/%s"%(self.user.username,filename)
		return ruta
	foto 			 =	models.ImageField(upload_to=url)
	genero           = models.CharField(max_length=50, choices = GENEROS)
	fecha_nacimiento = models.DateField()
	enfermedad       = models.ManyToManyField(Enfermedad, null= True, blank =True)
	user             = models.ForeignKey(User)

	def __unicode__ (self):
		return self.genero

	class Meta:
		verbose_name_plural = "Persona"



class Valoracion(models.Model):
	masamuscular    = models.CharField(max_length = 100)
	fecha_hora      = models.DateTimeField(auto_now_add = True)
	peso            = models.CharField(max_length=100)
	grasa_viceral   = models.CharField(max_length=100)
	grasa_corporal  = models.CharField(max_length=100)
	pagua           = models.CharField(max_length=100)
	masaosea        = models.CharField(max_length=100)
	edad_metabolica = models.CharField(max_length=100)
	bmr             = models.CharField(max_length=100)
	persona         = models.OneToOneField(Persona)
	

	def __unicode__ (self):
		return self.masamuscular

	class Meta:
		verbose_name_plural = "Valoracion"
	


