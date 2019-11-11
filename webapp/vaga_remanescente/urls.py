from django.urls import path
from vaga_remanescente.views import GetVagaByEscola, GetVagasFilter

urlpatterns = [

    path('<int:cd_serie>/', GetVagaByEscola.as_view(), name='vaga_escola'),
    path('filtros/', GetVagasFilter.as_view(), name='filtros'),
]
