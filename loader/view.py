#coding: utf-8

from django.shortcuts import render_to_response
#from django.templates import RequestContext

def run(request):
    return render_to_response('loader.html')