from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny
from rest_framework import status
import requests
from .models import *
from .serializers import *
from django.core.paginator import Paginator
from django.urls import reverse_lazy


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, ]

    def create(self, request, *args, **kwargs):
        data = request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'success': 'Comment has been created'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class ThingViewSet(ModelViewSet):
    serializer_class = ThingSerializer
    per_page = 20
    def get_permissions(self):
        if self.action == "list" or self.action == "retrieve":
            permission_classes = [AllowAny, ]
        else:
            permission_classes = [IsAdminUser, ]

        return [permission() for permission in permission_classes]


    def get_queryset(self):
        search_str = self.request.GET.get('string', '')
        queryset = Thing.objects.filter(title__icontains = search_str)
        return queryset
    

    def list(self, request, *args, **kwargs):
        page = int(self.request.GET.get('page', 1))
        queryset = self.get_queryset()
        pagination = Paginator(object_list=queryset, per_page=self.per_page)
        results = self.serializer_class(pagination.page(page), many=True).data
        
        previous = None
        next = None
        string = self.request.GET.get('string', '')

        if(page > 1):
            previous = reverse_lazy('thing') + f'?string={string}&page={page - 1}' 
        if(page < pagination.num_pages):
            next = reverse_lazy('thing') + f'?string={string}&page={page + 1}' 

        return Response(
            {
                'results': results,
                'previous_page': previous,
                'next_page': next,
                'page': page,
                
            }, 
            status=status.HTTP_202_ACCEPTED
        )   
   

class ParseThingsView(APIView):
    permission_classes = [IsAdminUser,]
    model_class = Thing
    serializer_class = ThingSerializer


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
