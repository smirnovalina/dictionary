from words.models import Words
from words.serializers import WordsSerializer
from rest_framework import generics


class WordList(generics.ListCreateAPIView):
    queryset = Words.objects.all()
    serializer_class = WordsSerializer


class WordDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Words.objects.all()
    serializer_class = WordsSerializer
