from fila_da_creche.queries.dt_atualizacao import get_dt_atualizacao
from fila_da_creche.queries.escolas import get_escolas
from fila_da_creche.queries.espera import get_espera
from rest_framework.response import Response
from rest_framework.views import APIView

from utils.get_raio import get_raio


class GetFilaByEscola(APIView):

    def get(self, request, cd_serie, lat, lon):
        resposta = {}
        raio = get_raio(cd_serie)

        # Queries no Banco do Fila da Creche
        resposta['espera'] = get_espera(cd_serie, lon, lat, raio)
        resposta['escolas'] = get_escolas(cd_serie, lon, lat, raio)
        resposta['dt_atualizacao'] = get_dt_atualizacao()

        return Response(resposta)
