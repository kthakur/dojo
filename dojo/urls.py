from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()
from settings import MEDIA_ROOT

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    (r'^site-media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': MEDIA_ROOT }),
    
    url(r'^getting_started/$', 'getting_started.views.getting_started',name='getting_started'),
    url(r'^classy/$', 'getting_started.views.classy',name='classy'),
    url(r'^template_widget/$', 'getting_started.views.template_widget',name='template_widget'),
    url(r'^dijit_layout/$', 'getting_started.views.dijit_layout',name='dijit_layout'),
    
    url(r'^flickr/$', 'flickr.views.flickr',name='flickr'),
)
