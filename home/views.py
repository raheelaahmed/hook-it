from django.shortcuts import render
from django.conf import settings


# Create your views here.

def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html', {"MEDIA_URL": settings.MEDIA_URL})


def about(request):
    """ A view to return the about page """

    return render(request, 'home/about.html', {"MEDIA_URL": settings.MEDIA_URL})