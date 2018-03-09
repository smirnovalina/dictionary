from words.models import Words
from django.contrib.auth.models import User
from words.serializers import WordsSerializer, UserSerializer
from words.permissions import IsOwner
from rest_framework import generics, permissions


class WordList(generics.ListCreateAPIView):
    queryset = Words.objects.all()
    serializer_class = WordsSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwner)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class WordDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Words.objects.all()
    serializer_class = WordsSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwner)


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
