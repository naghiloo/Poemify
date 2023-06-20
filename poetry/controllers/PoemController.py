from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from poetry.models import Status, Poem
from poetry.serializers import PoemSerializer

class PoemController(APIView):
    
    def get(self, request, poem_id):
        try:
            poem = Poem.objects.get(id=poem_id)
            serializer = PoemSerializer(poem)
            return Response(serializer.data)
        except Status.DoesNotExist:
            return Response({'error': 'Poem not found'}, status=404)