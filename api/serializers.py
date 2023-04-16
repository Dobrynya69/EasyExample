from rest_framework import serializers
from .models import *


class ThingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Thing
        fields = ('id', 'title', 'year', 'image')


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('author', 'thing', 'text')