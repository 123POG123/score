"""santex URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include
from fase.views import *



urlpatterns = [

    path('admin/', admin.site.urls, name='admin'),
    path('s/', template, name='start'),
    path('main/', firstPage, name='first'),
    path('delivery/', delivery, name='delivery'),
    path('buy/', buy, name='buy'),
    path('aboutTheStore/', aboutTheStore, name='aboutTheStore'),
    path('plumbing_installation/', plumbing_installation, name='plumbing_installation'),
    path('contact/', contact, name='contact'),
    path('mixer/', include('fase.urls')),


]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL)
