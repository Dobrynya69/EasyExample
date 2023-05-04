from django.urls import reverse, resolve
from django.test import SimpleTestCase
from api.views import *
from api.models import *
from rest_framework.test import APITestCase


class AnimeListAPIViewTests(APITestCase):
    anime_list_url = reverse('anime')
    model_class = Anime
    model_genre_class = Genre


    def setUp(self):
        self.model_genre_class.objects.create(name='genre1')
        self.model_genre_class.objects.create(name='genre2')
        self.model_genre_class.objects.create(name='genre3')

        anime1 = self.model_class.objects.create(title='title1', image='image1.jpg', description='description1')
        anime1.genres.set(({'genre1', 'genre2'}))
        anime1.save()

        anime2 = self.model_class.objects.create(title='title2', image='image2.jpg', description='description1')
        anime2.genres.set(({'genre2', 'genre1'}))
        anime2.save()

        anime3 = self.model_class.objects.create(title='title3', image='image3.jpg', description='description1')
        anime3.genres.set(({'genre3', 'genre1'}))
        anime3.save()


    def test_get_anime_list(self):
        response = self.client.get(self.anime_list_url)
        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)


class AnimeDetailAPIViewTests(APITestCase):
    anime_detail_url = reverse('anime_detail', kwargs={"pk": "1"})
    model_class = Anime
    model_genre_class = Genre


    def setUp(self):
        self.model_genre_class.objects.create(name='genre1')
        self.model_genre_class.objects.create(name='genre2')

        anime1 = self.model_class.objects.create(title='title1', image='image1.jpg', description='description1')
        anime1.genres.set(({'genre1', 'genre2'}))
        anime1.save()


    def test_get_anime_detail(self):
        response = self.client.get(self.anime_detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class GenreListViewTests(APITestCase):
    genre_list_url = reverse('genre')
    model_class = Genre


    def setUp(self):
        self.model_class.objects.create(name="genre1")
        self.model_class.objects.create(name="genre2")
        self.model_class.objects.create(name="genre3")


    def test_get_anime_detail(self):
        response = self.client.get(self.genre_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)