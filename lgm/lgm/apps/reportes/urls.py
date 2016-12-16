from django.conf.urls.defaults import patterns,url


urlpatterns = patterns('lgm.apps.reportes.views',
		url(r'^grafica/$', 'grafica_view', name = 'vista_grafica'),
		url(r'^reporte/$', 'reporte_view', name = 'vista_reporte'),
		url(r'^grasa/$', 'grasa_view', name = 'vista_grasa'),
		url(r'^viceral/$', 'viceral_view', name = 'vista_viceral'),
		url(r'^osea/$', 'osea_view', name = 'vista_osea'),
)
