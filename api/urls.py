from django.conf.urls import patterns, include, url

from rest_framework import routers
from django_app.quickstart import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

urlpatterns = patterns('',
    url(r'^', include(router.urls)),
)
