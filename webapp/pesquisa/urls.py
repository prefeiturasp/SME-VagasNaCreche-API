from django.conf.urls import url
from pesquisa.api.viewset_historico_busca_endereco import HistoricoBuscaEnderecoViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('historico_busca_end', HistoricoBuscaEnderecoViewSet, basename='historio_busca_endereco')


urlpatterns = router.urls