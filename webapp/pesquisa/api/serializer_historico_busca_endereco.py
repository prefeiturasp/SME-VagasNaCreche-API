from pesquisa.models import HistoricoBuscaEndereco
from rest_framework import serializers


class HistoricoBuscaEnderecoSerializer(serializers.ModelSerializer):

    class Meta:

        model = HistoricoBuscaEndereco
        fields = ('latitude', 'longitude', 'cd_serie')