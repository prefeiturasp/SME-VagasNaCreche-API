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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from fila_da_creche.urls import urlpatterns as fila_da_creche_urls
from helloapp.views import HelloWorld
from pesquisa.urls import urlpatterns as pesquisa_urls
from rest_framework.permissions import AllowAny
from vaga_remanescente.urls import urlpatterns as vaga_urls

# router = routers.DefaultRouter()

schema_view_sp360 = get_schema_view(
    openapi.Info(
        title="API Vaga na Creche",
        default_version='v1',
        description='',
        contact=openapi.Contact(email="giuseppe.rosa@amcom.com.br"),
    ),
    # url='https://hom-vaganacreche.sme.prefeitura.sp.gov.br/api',
    public=True,
    permission_classes=(AllowAny,)
)

urlpatterns = [
    # path('api/', include(router.urls)),
    url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view_sp360.without_ui(cache_timeout=0), name='schema-json'),
    path('', schema_view_sp360.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('hello/', HelloWorld.as_view()),
    path('admin/', admin.site.urls),
    path('pesquisa/', include(pesquisa_urls), name='pesquisa'),
    path('fila/', include(fila_da_creche_urls), name='fila-da-creche'),
    path('vaga/', include(vaga_urls), name='vaga'),
]
