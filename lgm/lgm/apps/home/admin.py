from django.contrib import admin
from lgm.apps.home.models import Clase, Enfermedad, Ejercicio, Rutina, Producto, Dieta, Valoracion, User, Persona
from lgm.apps.home.models import user_profile


admin.site.register(Clase)
admin.site.register(Enfermedad)
admin.site.register(Ejercicio)
admin.site.register(Rutina)
admin.site.register(Producto)
admin.site.register(Dieta)
admin.site.register(Valoracion)
admin.site.register(Persona)
admin.site.register(user_profile)
