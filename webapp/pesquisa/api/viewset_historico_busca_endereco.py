from pesquisa.api.serializer_historico_busca_endereco import HistoricoBuscaEnderecoSerializer
from pesquisa.models import HistoricoBuscaEndereco

from rest_framework.viewsets import ModelViewSet


class HistoricoBuscaEnderecoViewSet(ModelViewSet):

    queryset = HistoricoBuscaEndereco.objects.all()
    serializer_class = HistoricoBuscaEnderecoSerializer
    http_method_names = ['post']
