from django.conf.urls import patterns, url, include
from portfolio import views

urlpatterns = patterns('',
    url(r'^$', 'portfolio.views.index', name='index'),

    url(r'^category/(?P<pk>\d+)/$',
        'portfolio.views.category_photos',
        name="category_photos"),

    url(r'start$',
        views.start,
        name="start"),

    #url(r'ajax-upload$',
    #    UploadView.as_view(),
    #    name="ajax_upload"),


    #API
    url(r'^api/$', views.api_root),

    url(r'^api/photos/$',
        views.photo_list.as_view(),
        name='photo-list'),

    url(r'^api/photos/(?P<pk>[0-9]+)$',
        views.photo_detail.as_view(),
        name='photo-detail'),

    url(r'^api/categories/$',
        views.category_list.as_view(),
        name='category-list'),

    url(r'^api/categories/(?P<pk>[0-9]+)$',
        views.category_detail.as_view(),
        name='category-detail'),
)
