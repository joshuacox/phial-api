from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings

from rest_framework import routers

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    #API
    url(r'^api/', include('phial_api.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'', include('web.urls')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
