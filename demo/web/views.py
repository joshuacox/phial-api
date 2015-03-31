from django.conf import settings
from phial_api.models import Category, Photo

from django.shortcuts import render, redirect
from django.middleware.csrf import get_token

def index(request):
    categories = Category.objects.all()
    context = {
            'categories': categories,
            'csrf_token': get_token(request),
        }
    return render(request, 'web/index.html', context)

def category_photos(request, pk):
    categories = Category.objects.all()
    selected = Category.objects.filter(id=pk)[0]

    return render(request, 'web/individual-category.html', {'categories': categories, 'selected': selected})

def start(request):
    #Only logged in users can upload
    if not request.user.is_authenticated():
        return redirect('/admin/login/?next=%s' % request.path)

    context = {
        'categories': Category.objects.all(),
        'AWS_EXPECTED_BUCKET': settings.AWS_EXPECTED_BUCKET,
        'AWS_UPLOAD_CLIENT_KEY': settings.AWS_UPLOAD_CLIENT_KEY,
        'csrf_token': get_token(request),
    }
    return render(request, 'web/upload.html', context)
