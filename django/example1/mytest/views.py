from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader, RequestContext

from datetime import datetime

def index (request):
    return HttpResponse( 'JKKLHKLHklk' )

def curtime (request):
    Text = 'Server time {0}'.format (datetime.now())
    return HttpResponse( Text)

def people (request):
    template = loader.get_template('mytest/index.html')
    context = RequestContext (request, {})
    return HttpResponse( template.render(context))
