from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)


admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    #API
    url(r'^g/', include('portfolio.urls')),
    url(r'^', include(router.urls)),
    url(r'^upload/', include('django_fine_uploader.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)
