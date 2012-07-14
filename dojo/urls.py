from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()
from settings import MEDIA_ROOT

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    (r'^site-media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': MEDIA_ROOT }),
    
    url(r'^homepage/$', 'getting_started.views.homepage',name='homepage'),
)
