from django.conf.urls.defaults import patterns,url


urlpatterns = patterns('lgm.apps.admin.views',
		url(r'^enfermedad/(?P<id_prod>.*)/$', 'single_enfermedad_view', name = 'vista_single_enfermedad'),
		url(r'^add/enfermedad/$','add_enfermedad_view',name = 'vista_agregar_enfermedad'),	
		url(r'^edit/enfermedad/(?P<id_prod>.*)/$','edit_enfermedad_view',name = 'vista_editar_enfermedad'),
		url(r'^del/enfermedad/(?P<id_prod>.*)/$','del_enfermedad_view',name ='vista_eliminar_enfermedad'),
		url(r'^enfermedades/page/(?P<pagina>.*)/$', 'enfermedades_view', name = 'vista_enfermedades'),
		url(r'^add/tipo_enfermedades/$','add_tipo_enfermedades_view',name = 'vista_agregar_tipo'),	
		url(r'^del/tipo_enfermedad/(?P<id_prod>.*)/$','del_tipo_enfermedad_view',name ='vista_eliminar_tipo_enfermedad'),


)