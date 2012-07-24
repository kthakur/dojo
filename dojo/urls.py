from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()
from settings import MEDIA_ROOT
from django.conf.urls.defaults import *
from getting_started.api import EntryResource, UserResource
from tastypie.api import Api

v1_api = Api(api_name='v1')
v1_api.register(UserResource())
v1_api.register(EntryResource())

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    (r'^site-media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': MEDIA_ROOT }),
    
    url(r'^getting_started/$', 'getting_started.views.getting_started',name='getting_started'),
    url(r'^classy/$', 'getting_started.views.classy',name='classy'),
    url(r'^template_widget/$', 'getting_started.views.template_widget',name='template_widget'),
    url(r'^dijit_layout/$', 'getting_started.views.dijit_layout',name='dijit_layout'),
    url(r'^datagrid/$', 'getting_started.views.datagrid',name='datagrid'),
    
    url(r'^flickr/$', 'flickr.views.flickr',name='flickr'),
    
    (r'^api/', include(v1_api.urls)),
)