from django.shortcuts import render
from django.http import HttpResponse

from . import models
# Create your views here.


def home(request):

    return render(request, 'home/index.html', {'post': models.Articles.objects.all()})


def base(request):
    return render(request, 'home/base.html')