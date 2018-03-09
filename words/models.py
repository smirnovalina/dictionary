import json
from django.db import models


class Words(models.Model):
    english_word = models.CharField(max_length=100)
    russian_translation = models.CharField(max_length=200)
    rating = models.IntegerField(default=0)

    owner = models.ForeignKey('auth.User', related_name='words', on_delete=models.CASCADE)

    def set_translation(self, translation):
        self.russian_translation = json.dumps(translation, separators=(',', ':'))

    def get_translation(self):
        return json.loads(self.russian_translation)