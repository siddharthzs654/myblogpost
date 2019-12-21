from django.contrib import admin
from django.urls import path, include

from users import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home.urls')),
    path('register/', views.register, name="blog-register")
]


