from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny
from rest_framework import status
import requests
from .models import *
from .serializers import *
from django.core.paginator import Paginator
from django.db.models import Q
from django.urls import reverse_lazy
import sched, time


#A view for creating comments to some title. Access only to lged in users.
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


#A view for getting a list of all genres. Access only to anybody.
class GenreView(APIView):
    model_class = Genre
    serializer_class = GenreSerializer

    def get_queryset(self):
        return self.model_class.objects.filter(~Q(name="No genres"))
    

    def get(self, request, *args, **kwargs):
        results = self.serializer_class(self.get_queryset(), many=True).data
        return Response({'genres': results}, status=status.HTTP_202_ACCEPTED) 


#A view set for creating, deletation, editing, filtering, anime. Access depends on request.
class AnimeViewSet(ModelViewSet):
    serializer_class = AnimeSerializer
    per_page = 20


    def get_permissions(self):
        if self.action == "list" or self.action == "retrieve" or self.action == "filter":
            permission_classes = [AllowAny, ]
        else:
            permission_classes = [IsAdminUser, ]

        return [permission() for permission in permission_classes]


    def get_queryset(self):
        search_str = self.request.GET.get('string', '')
        queryset = Anime.objects.filter(title__icontains = search_str)
        return queryset
    

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        page = int(self.request.GET.get('page', 1))
        pagination = Paginator(object_list=queryset, per_page=self.per_page)
        results = self.serializer_class(pagination.page(page), many=True).data
        
        previous = None
        next = None
        string = self.request.GET.get('string', '')

        if(page > 1):
            previous = reverse_lazy('anime') + f'?string={string}&page={page - 1}' 
        if(page < pagination.num_pages):
            next = reverse_lazy('anime') + f'?string={string}&page={page + 1}' 

        return Response(
            {
                'results': results,
                'previous_page': previous,
                'next_page': next,
                'page': page, 
                'max_page': pagination.num_pages
            }, 
            status=status.HTTP_202_ACCEPTED
        )   
    
    
    def filter(self, request, *args, **kwargs):  
        queryset = self.get_queryset()
        genres_data = request.data.get('genres', [])
        if type(genres_data) == str:
            genres_data = [genres_data,]
        if len(genres_data) > 0:
            for genre in genres_data:
                queryset = queryset.filter(genres = genre)

        page = int(self.request.GET.get('page', 1))
        pagination = Paginator(object_list=queryset, per_page=self.per_page)
        results = self.serializer_class(pagination.page(page), many=True).data
        
        previous = None
        next = None
        string = self.request.GET.get('string', '')

        if(page > 1):
            previous = reverse_lazy('anime') + f'?string={string}&page={page - 1}' 
        if(page < pagination.num_pages):
            next = reverse_lazy('anime') + f'?string={string}&page={page + 1}' 

        return Response(
            {
                'results': results,
                'previous_page': previous,
                'next_page': next,
                'page': page, 
                'max_page': pagination.num_pages,
                'filter_data': {'genres': genres_data}
            }, 
            status=status.HTTP_202_ACCEPTED
        )
   
#A view for parse anime list api. Access only to admin.
class ParseAnimesView(APIView):
    permission_classes = [IsAdminUser,]
    model_class = Anime
    genre_class = Genre
    serializer_class = AnimeSerializer
    genre_serializer_class = GenreSerializer


    def addGenres(self, genres):
        if genres is None:
            genres = ['No genres',]

        for genre in genres:
            try:
                self.genre_class.objects.get(name=genre)
            except self.genre_class.DoesNotExist:
                serializer = self.genre_serializer_class(data={'name': genre})
                if serializer.is_valid():
                    serializer.save()
                else:
                    return Response({'message': serializer.errors}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return genres


    def post(self, request, *args, **kwargs):
        self.model_class.objects.all().delete()
        for _ in range(100):
            response = requests.get("https://api.jikan.moe/v4/random/anime").json()
            if "data" in response:
                genres = []
                for genre in response["data"]["genres"]:
                    genre, _ = self.genre_class.objects.get_or_create(name=genre["name"])
                    genres.append(genre)
                model_object, created = self.model_class.objects.get_or_create(
                    title=response["data"]["title"],
                    description=response["data"]["synopsis"] if response["data"]["synopsis"] else "",
                    image=response["data"]["images"]["jpg"]["image_url"])
                if created:
                    model_object.genres.set(genres)
            time.sleep(2)
        return Response(status=status.HTTP_201_CREATED)
