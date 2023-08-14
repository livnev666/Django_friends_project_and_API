from rest_framework import serializers
from .models import Movie, Actor, Director, CommentUser


class MovieSerializer(serializers.ModelSerializer):

    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Movie
        fields = ['id', 'user', 'name', 'years', 'content', 'rating', 'director', 'slug']


class CommentSerializer(serializers.ModelSerializer):

    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = CommentUser
        fields = '__all__'