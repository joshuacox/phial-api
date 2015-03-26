from django.conf.urls import patterns, url, include
from flex_api import views

urlpatterns = patterns('',
    url(r'^$', views.api_root),

    url(r'^photos/$',
        views.photo_list.as_view(),
        name='photo-list'),

    url(r'^photos/(?P<pk>[0-9]+)$',
        views.photo_detail.as_view(),
        name='photo-detail'),

    url(r'^categories/$',
        views.category_list.as_view(),
        name='category-list'),

    url(r'^categories/(?P<pk>[0-9]+)$',
        views.category_detail.as_view(),
        name='category-detail'),
)
