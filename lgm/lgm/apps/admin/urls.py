from django.conf.urls.defaults import patterns,url


urlpatterns = patterns('lgm.apps.admin.views',
		url(r'^enfermedad/(?P<id_prod>.*)/$', 'single_enfermedad_view', name = 'vista_single_enfermedad'),
		url(r'^add/enfermedad/$','enfermedad_producto_view',name = 'vista_agregar_enfermedad'),	
		url(r'^edit/enfermedad/(?P<id_prod>.*)/$','edit_enfermedad_view',name = 'vista_editar_enfermedad'),
		url(r'^del/enfermedad/(?P<id_prod>.*)/$','del_enfermedad_view',name ='vista_eliminar_enfermedad'),
		url(r'^enfermedades/page/(?P<pagina>.*)/$', 'enfermedades_view', name = 'vista_enfermedades'),
		url(r'^add/tipo_enfermedades/$','add_tipo_enfermedades_view',name = 'vista_agregar_tipo'),	
		url(r'^del/tipo_enfermedad/(?P<id_prod>.*)/$','del_tipo_enfermedad_view',name ='vista_eliminar_tipo_enfermedad'),

		url(r'^enfermedad_producto/$','enfermedad_producto_view',name = 'enfermedad_producto'),	
		url(r'^producto/(?P<id_prod>.*)/$', 'single_producto_view', name = 'vista_single_producto'),
		url(r'^add/productos/$','add_producto_view',name = 'vista_agregar_producto'),	
		url(r'^edit/productos/(?P<id_prod>.*)/$','edit_producto_view',name = 'vista_editar_producto'),
		url(r'^del/productos/(?P<id_prod>.*)/$','del_producto_view',name ='vista_eliminar_producto'),
		url(r'^productos/page/(?P<pagina>.*)/$', 'productos_view', name = 'vista_productos'),
		url(r'^add/tipo_producto/$','add_tipo_productos_view',name = 'vista_tipo_prod'),	
		url(r'^del/tipo_producto/(?P<id_prod>.*)/$','del_tipo_producto_view',name ='vista_eliminar_tipo_producto'),



)