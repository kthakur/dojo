from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.sites.models import RequestSite
from django.contrib.sites.models import Site

def flickr(request):
    site = RequestSite(request)
    return render_to_response('flickr.html', {'site':site}, RequestContext(request))
