from flexgallery.models import Category, Photo
from flexgallery.serializers import PhotoSerializer, CategorySerializer
from rest_framework import generics, permissions

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from django.shortcuts import render
from django.middleware.csrf import get_token

class photo_list(generics.ListCreateAPIView):
    """
    List all photos, or create a new photo
    """
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

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


class category_detail(generics.RetrieveUpdateDestroyAPIView):
    """
    CRUD for categories
    """
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

@api_view(('GET',))
def api_root(request, format=None):
    return Response({
        'categories': reverse('category-list', request=request, format=format),
        'photo': reverse('photo-list', request=request, format=format)
    })

"""
Web - abstract below this line seperate app meant for public facing things
"""


def index(request):
    categories = Category.objects.select_related('photos')
    context = {'categories': categories}
    return render(request, 'flexgallery/index.html', context)

def category_photos(request, pk):
    categories = Category.objects.all()
    selected = Category.objects.filter(id=pk)[0]

    return render(request, 'flexgallery/individual-category.html', {'categories': categories, 'selected': selected})

def start(request):
    context = { 'categories': Category.objects.all(), 'csrf_token': get_token(request), }
    return render(request, 'flexgallery/import.html', context)
