from django.conf.urls import patterns, url, include
from web import views

urlpatterns = patterns('',
    url(r'^$', 'web.views.index', name='index'),

    url(r'^category/(?P<pk>\d+)/$',
        'web.views.category_photos',
        name="category_photos"),

    url(r'start$',
        views.start,
        name="start"),

    url(r'ajax-upload$',
        views.uploader,
        name="ajax_upload"),
)
