from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from ncsBackend.restAPI.utils import read_json

@api_view(['GET'])
def api_movies_view(request):

    print("LOG: request", request.query_params)
    if request.method == 'GET':
        responseData = { 'total': 0, 'entries': [] }

        queryParams = request.query_params
        
        data = read_json('ncsBackend/restAPI/sample.json')
        entries = data['entries']

        if 'filterBy' in queryParams:
            filterByValue = queryParams['filterBy'].split(':')[1]
            entries = [entry for entry in entries if entry['programType'] == filterByValue]

        if 'searchBy' in queryParams:
            searchByKey = queryParams['searchBy'].split(':')[0]
            searchByValue = queryParams['searchBy'].split(':')[1]

            if searchByKey == 'releaseYear':
                entries = [entry for entry in entries if entry['releaseYear'] >= int(searchByValue)]
            elif searchByKey == 'title':
                entries = [entry for entry in entries if entry['title'].lower().find(searchByValue.lower()) != -1]

        if 'sortBy' in queryParams:
            sortByKey = queryParams['sortBy'].split(':')[0]
            sortByValue = queryParams['sortBy'].split(':')[1]
            sortReverse = False
            if sortByValue == 'desc': sortReverse = True

            entries.sort(key=lambda x: x[sortByKey], reverse=sortReverse)

        if 'count' in queryParams:
            entries = entries[:int(queryParams['count'])]


        responseData['entries'] = entries
        responseData['total'] = len(entries)

        return Response(responseData, status.HTTP_200_OK)