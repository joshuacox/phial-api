from flexgallery.models import Category, Photo
from django_fine_uploader.views import AjaxFileUploader

from django.shortcuts import render
from django.middleware.csrf import get_token

def index(request):
    categories = Category.objects.select_related('photos')
    context = {'categories': categories}
    return render(request, 'web/index.html', context)

def category_photos(request, pk):
    categories = Category.objects.all()
    selected = Category.objects.filter(id=pk)[0]

    return render(request, 'web/individual-category.html', {'categories': categories, 'selected': selected})

def start(request):
    context = { 'categories': Category.objects.all(), 'csrf_token': get_token(request), }
    return render(request, 'web/import.html', context)

uploader = AjaxFileUploader()
