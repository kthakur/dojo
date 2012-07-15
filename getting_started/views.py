from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.sites.models import RequestSite
from django.contrib.sites.models import Site

def getting_started(request):
    site = RequestSite(request)
    #site = Site.objects.get_current()
    return render_to_response('getting_started.html', {'site':site}, RequestContext(request))

def classy(request):
    site = RequestSite(request)
    return render_to_response('classy.html', {'site':site}, RequestContext(request))

def template_widget(request):
    site = RequestSite(request)
    return render_to_response('template_widget.html', {'site':site}, RequestContext(request))

def dijit_layout(request):
    site = RequestSite(request)
    return render_to_response('dijit_layout.html', {'site':site}, RequestContext(request))
