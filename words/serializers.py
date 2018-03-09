from rest_framework import serializers
from words.models import Words


class WordsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Words
        fields = ('id', 'english_word', 'russian_translation', 'rating')
