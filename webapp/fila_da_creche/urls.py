from django.urls import path
from fila_da_creche.views import GetFilaByEscola

urlpatterns = [

    path('espera_escola_raio/<str:lat>/<str:lon>/<int:cd_serie>', GetFilaByEscola.as_view(),
         name='espera_escola_raio'),
]