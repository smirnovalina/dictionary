from rest_framework import serializers
from words.models import Words
from django.contrib.auth.models import User


class WordsSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Words
        fields = ('id', 'english_word', 'russian_translation', 'rating', 'owner')


class UserSerializer(serializers.ModelSerializer):
    words = serializers.PrimaryKeyRelatedField(many=True, queryset=Words.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'words')
