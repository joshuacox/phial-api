from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

from rest_framework import routers

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^blog/', include('blog.urls')),

    url(r'^g/', include('web.urls')),
    url(r'^admin/', include(admin.site.urls)),

    #API
    url(r'^api/', include('flexgallery.urls')),
    url(r'^upload/', include('django_fine_uploader.urls', namespace='django_fine_uploader')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)
