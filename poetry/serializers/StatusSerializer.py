import random
from rest_framework import serializers

from poetry.models import Status

from poetry.serializers import PoemSerializer

class StatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = Status
        fields = ['code', 'description', 'category']
        # exclude = ['id']


class PoemByStatusCodeSerializer(serializers.ModelSerializer):
    poem = serializers.SerializerMethodField()

    class Meta:
        model = Status
        fields = ['code', 'description', 'category', 'poem']

    
    def get_poem(self, status):
        poems = status.poems.all()
        random_poem = random.choice(poems)
        poem_serializer = PoemSerializer(random_poem)
        return poem_serializer.data