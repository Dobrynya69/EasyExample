from django.urls import path, reverse, include, resolve
from django.test import SimpleTestCase
from api.views import *
from api.models import *
from rest_framework.test import APITestCase, APIClient
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.views import APIView


class ApiUrlsTests(SimpleTestCase):

    def test_anime_list_url(self):
        url = reverse('anime')
        self.assertEquals(resolve(url).func.view_class, AnimeViewSet)


    def test_genre_list_url(self):
        url = reverse('genre')
        self.assertEquals(resolve(url).func.view_class, GenreView)


class AnimeListAPIViewTests(APITestCase):
    anime_list_url = reverse('anime')
    model_class = Anime
    model_genre_class = Genre


    def setUp(self):
        self.model_genre_class.objects.create(name='genre1')
        self.model_genre_class.objects.create(name='genre2')
        self.model_genre_class.objects.create(name='genre3')

        self.model_class.objects.create(title='title1', image='image1.jpg', genres={'genre1', 'genre2'}, description='description1')
        self.model_class.objects.create(title='title2', image='image2.jpg', genres={'genre2', 'genre1'}, description='description1')
        self.model_class.objects.create(title='title3', image='image3.jpg', genres={'genre3', 'genre1'}, description='description1')


    def test_get_anime_list(self):
        response = self.client.get(self.anime_list_url)
        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)