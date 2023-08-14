from django.shortcuts import render
from rest_framework import generics
from rest_framework.decorators import action
from rest_framework.response import Response
from .permissions import IsAdminReadOnlyUpdate, IsAdminReadOnlyDelete
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated
from .models import Movie, Actor, Director, CommentUser
from .serializers import MovieSerializer, CommentSerializer
from rest_framework.pagination import PageNumberPagination


class MovieAPIPagination(PageNumberPagination):

    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 10


class MovieAPIListCreate(generics.ListCreateAPIView):

    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )
    pagination_class = MovieAPIPagination


class MovieAPIUpdate(generics.RetrieveUpdateAPIView):

    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = (IsAdminReadOnlyUpdate, )


class MovieAPIDelete(generics.RetrieveDestroyAPIView):

    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = (IsAdminReadOnlyDelete, )


# COMMENTARY
class CommentAPIListCreate(generics.ListCreateAPIView):

    queryset = CommentUser.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )
    pagination_class = MovieAPIPagination


class CommentAPIUpdate(generics.RetrieveUpdateAPIView):

    queryset = CommentUser.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (IsAdminReadOnlyUpdate, )


class CommentAPIDelete(generics.RetrieveDestroyAPIView):

    queryset = CommentUser.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (IsAdminReadOnlyDelete, )