from phial_api.models import Category, Photo
from django.contrib.auth.models import User
from phial_api.serializers import PhotoSerializer, CategorySerializer, UserSerializer
from rest_framework import generics, permissions

from rest_framework.parsers import MultiPartParser, FormParser, FileUploadParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from django.shortcuts import render
from django.middleware.csrf import get_token

# import the logging library
import logging

# Get an instance of a logger
logger = logging.getLogger('django')


class photo_list(generics.ListCreateAPIView):
    """
    List all photos, or create a new photo
    """
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
    parser_classes = (MultiPartParser, FormParser )

    def perform_create(self, serializer):
        data = self.request.data
        cat = data.get('category')
        serializer.save(category=Category.objects.get(pk=cat),)

    #def post(self, request, *args, **kwargs):
    #    """
    #    handle file uploads
    #    """
    #    logger.info('post:')
    #    logger.info(dict(request.data))

    #    self.create(request, *args, **kwargs)

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `gid` query parameter in the URL.
        """
        queryset = Photo.objects.all()
        gid = self.request.QUERY_PARAMS.get('gid', None)
        if gid is not None:
            queryset = queryset.filter(category=gid)
        return queryset



class photo_detail(generics.RetrieveUpdateDestroyAPIView):
    """
    CRUD for single photo
    """
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class category_list(generics.ListCreateAPIView):
    """
    List all categories, or create a new photo
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class category_detail(generics.RetrieveUpdateDestroyAPIView):
    """
    CRUD for categories
    """
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


@api_view(('GET',))
def api_root(request, format=None):
    return Response({
        'categories': reverse('category-list', request=request, format=format),
        'photo': reverse('photo-list', request=request, format=format),
        'users': reverse('user-list', request=request, format=format),
    })
