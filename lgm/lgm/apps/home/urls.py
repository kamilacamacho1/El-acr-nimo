from django.conf.urls.defaults import patterns,url


urlpatterns = patterns('lgm.apps.home.views',
		url(r'^$','index_view', name = 'vista_principal'),
		url(r'^login/$', 'login_view', name = 'vista_login'),
		url(r'^registro/$', 'register_view', name = 'vista_registro'),
		url(r'^logout/$', 'logout_view', name = 'vista_logout'),
		url(r'^about/$', 'about_view', name = 'vista_about'),
		url(r'^contact/$', 'contact_view', name = 'vista_contact'),
		url(r'^mapa/$', 'mapa_view', name = 'vista_mapa'),
		url(r'^coords/save$', 'coords_save', name = 'coords_save'),
		url(r'^ubicaciones/$', 'ubicaciones_view', name = 'vista_ubicaciones'),
		url(r'^dato/$', 'dato_view', name = 'vista_dato'),
		url(r'^seleccionar_enfermedades$', 'seleccionar_enfermedades_view', name = 'vista_seleccionar'),
#graficas
		url(r'^grafica/$', 'grafica_view', name = 'vista_grafica'),
		url(r'^reporte/$', 'reporte_view', name = 'vista_reporte'),
		url(r'^grasa/$', 'grasa_view', name = 'vista_grasa'),
		url(r'^viceral/$', 'viceral_view', name = 'vista_viceral'),
		url(r'^osea/$', 'osea_view', name = 'vista_osea'),
#graficas

		url(r'^nutricion/$', 'nutricion_view', name = 'vista_nutricion'),
		url(r'^valoraciones/$', 'valoraciones_view', name = 'vista_valoraciones'),
		url(r'^agregar/valoracion/$', 'tanita_view', name = 'vista_tanita'),
		

)


