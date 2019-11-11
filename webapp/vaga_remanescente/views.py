from fila_da_creche.queries.dt_atualizacao import get_dt_atualizacao
from rest_framework.response import Response
from rest_framework.views import APIView
from vaga_remanescente.queries.distrito import get_distritos
from vaga_remanescente.queries.dre import get_dre
from vaga_remanescente.queries.sub_prefeitura import get_sub_prefeituras
from vaga_remanescente.queries.vaga_por_escolas import get_vaga_por_escolas


class GetVagaByEscola(APIView):

    def get(self, request, cd_serie):
        resposta = {}
        filtro = request.GET.get('filtro', '')
        busca = request.GET.get('busca', '')

        if cd_serie not in [1, 4, 27, 28]:
            return Response('Série invalida')

        # Queries no Banco no DW
        resposta['escolas'] = get_vaga_por_escolas(filtro, busca, cd_serie)
        resposta['dt_atualizacao'] = get_dt_atualizacao()

        return Response(resposta)


class GetVagasFilter(APIView):
    def get(self, request):
        return Response({'dres': get_dre(),
                         'distritos': get_distritos(),
                         'sub-prefeituas': get_sub_prefeituras()})
