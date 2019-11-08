"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path, include
from helloapp.views import HelloWorld
from rest_framework import routers
from pesquisa.urls import urlpatterns as pesquisa_urls
from fila_da_creche.urls import urlpatterns as fila_da_creche_urls


router = routers.DefaultRouter()

urlpatterns = [
    path('api/', include(router.urls)),
    path('hello/', HelloWorld.as_view()),
    path('admin/', admin.site.urls),
    path('pesquisa/', include(pesquisa_urls), name='pesquisa'),
    path('fila-da-creche/', include(fila_da_creche_urls), name='fila-da-creche')
]

