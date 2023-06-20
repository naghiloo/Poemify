from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from poetry.models import Status, Poem
from poetry.serializers import PoemByStatusCodeSerializer

class PoemByStatusCodeController(APIView):
    
    def get(self, request, status_code):
        try:
            status = Status.objects.get(code=status_code)
        except Status.DoesNotExist:
            return Response({'error': 'Status code not found'}, status=404)
        
        serializer = PoemByStatusCodeSerializer(status)
        return Response(serializer.data)