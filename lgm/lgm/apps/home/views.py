# Create your views here.
from django.shortcuts import render_to_response, render
from django.template import RequestContext

def index_view (request):
	return render_to_response('home/index.html', context_instance = RequestContext(request))