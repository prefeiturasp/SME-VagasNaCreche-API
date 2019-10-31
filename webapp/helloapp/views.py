from rest_framework.response import Response
from rest_framework.views import APIView


class HelloWorld(APIView):
    def get(self, request):
        """
        Função inaugural
        :param request: Requisição HTTP
        :return: JSON com um lindo Hello World
        """
        return Response({'result': 'Hello World!!'})
