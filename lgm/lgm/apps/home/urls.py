from django.conf.urls.defaults import patterns,url


urlpatterns = patterns('lgm.apps.home.views',
		url(r'^$','index_view', name = 'vista_principal'),
		url(r'^add/clase/$','add_clase_view', name = 'vista_agregar_clase'),
)

