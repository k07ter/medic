#coding: utf-8

from django.shortcuts import render_to_response
from django.templates import RequestContext
from forms import LoaderForm

def run(request):
    ldr = LoaderForm()
    return render_to_response('loader.html', {'form': ldr}
 	 		       instance_context=RequestContext(request))
