from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from ncsBackend.restAPI.utils import read_json

@api_view(['GET'])
def api_movies_view(request):

    print("LOG: request", request)
    if request.method == 'GET':
        data = read_json('ncsBackend/restAPI/sample.json')
        return Response(data, status.HTTP_200_OK)