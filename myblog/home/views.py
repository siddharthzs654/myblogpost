from django.shortcuts import render
from django.http import HttpResponse

from .models import Posts
# Create your views here.

content = {
    'posts': Posts.objects.all()
}

def home(request):
    return render(request, 'home/index.html',content)

