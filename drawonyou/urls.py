from django.conf.urls.defaults import *
from django.conf import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^drawonyou/', include('drawonyou.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),

    (r'^$', 'drawonyou.draw.views.index'),
    (r'^friend_photo/?$', 'drawonyou.draw.views.friend_photo'),
    (r'^retrieve_photo/?$', 'drawonyou.draw.views.retrieve_photo'),
    (r'^upload_photo/?$', 'drawonyou.draw.views.upload_photo'),
)
if settings.DEVELOPMENT_MODE:
    urlpatterns += patterns('',
        (r'^(?P<path>.*)$', 'django.views.static.serve',
         {'document_root': '/Users/ericconner/Documents/draw'}),
    )
