from django.urls import path
from ncsBackend.restAPI.api.views import api_movies_view

app_name = 'restAPI'

urlpatterns = [
    path('movies', api_movies_view, name='movies')
]