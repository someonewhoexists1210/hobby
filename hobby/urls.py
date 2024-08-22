"""
URL configuration for hobby project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.shortcuts import render
from django.conf.urls import handler400, handler404, handler500

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('front.urls')),
]


def custom_400_error(request, exception):
    return render(request, '400.html', status=400)

def custom_404_error(request, exception):
    return render(request, '404.html', status=404)

def custom_500_error(request):
    return render(request, '500.html', status=500)

handler400 = custom_400_error
handler404 = custom_404_error
handler500 = custom_500_error