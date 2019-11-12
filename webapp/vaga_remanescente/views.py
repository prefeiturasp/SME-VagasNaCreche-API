import pickle
import zlib

from django.core.cache import cache
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
        cache_time = 3600
        cached_item = cache.get('filtros_vaga')
        if not cached_item:
            response = {'dres': get_dre(),
                        'distritos': get_distritos(),
                        'sub-prefeituras': get_sub_prefeituras()}
            cache.set('filtros_vaga', zlib.compress(pickle.dumps(response)), cache_time)
            return Response(response)
        print('Com cache')
        return Response(pickle.loads(zlib.decompress(cached_item)))
