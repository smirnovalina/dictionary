from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework import permissions, status
from words.models import Words
from django.contrib.auth.models import User
from words.serializers import WordsSerializer, UserSerializer
from words.permissions import IsOwner


class WordList(APIView):
    """
    List all words, or create a new word.
    """
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'words/index.html'

    def get(self, request):
        words = Words.objects.all()
        self.check_object_permissions(request, words)
        serializer = WordsSerializer(words, many=True)
        return Response({'words': words})

    def post(self, request):
        serializer = WordsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class WordDetail(APIView):
    """
    Retrieve, update or delete a word instance.
    """
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwner)

    def get(self, request, pk):
        word = get_object_or_404(Words, pk=pk)
        self.check_object_permissions(request, word)
        serializer = WordsSerializer(word)
        return Response(serializer.data)

    def put(self, request, pk):
        word = get_object_or_404(Words, pk=pk)
        self.check_object_permissions(request, word)
        serializer = WordsSerializer(word, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        word = get_object_or_404(Words, pk=pk)
        self.check_object_permissions(request, word)
        word.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserList(APIView):
    """
    List all users.
    """
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)


class UserDetail(APIView):
    """
    Retrieve a user instance.
    """
    def get(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)
