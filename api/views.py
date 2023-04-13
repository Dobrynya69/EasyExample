from io import BytesIO
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from rest_framework import status
from PIL import Image
from django.core.files import File
import requests
from .models import *
from .serializers import *

class ExampleView(APIView):
    def get(self, request, *args, **kwargs):
        return Response({'you': 'sucker'}, status=status.HTTP_200_OK)
    

class ParseMoviesView(APIView):
    permission_classes = [IsAdminUser,]
    model_class = Movie
    serializer_class = MovieSerializer


    def post(self, request, *args, **kwargs):
        self.model_class.objects.all().delete()
        movies_created = 0
        page = 1
        while(movies_created <= 100):
            url = "https://moviesdatabase.p.rapidapi.com/titles/"
            querystring = {"page": page, "startYear": 2015}
            headers = {
                "X-RapidAPI-Key": "3ac8f1a79amsh99e49430e0195f2p15d2e7jsn0b9cc08b17b8",
                "X-RapidAPI-Host": "moviesdatabase.p.rapidapi.com"
            }
            response = requests.request("GET", url, headers=headers, params=querystring).json()
            for movie in response['results']:
                if movie['primaryImage'] is not None:
                    serializer = self.serializer_class(data={'title': movie['titleText']['text'], 'year': movie['releaseYear']['year'], 'image': movie['primaryImage']['url']})
                    if serializer.is_valid():
                        serializer.save()
                        movies_created += 1
                    else:
                        return Response({'message': serializer.errors}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            page += 1

        return Response({'message': 'success'}, status=status.HTTP_201_CREATED)
