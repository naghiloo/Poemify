from rest_framework import serializers

from poetry.models import Poem

class PoemSerializer(serializers.ModelSerializer):
    # status = StatusSerializer(read_only=True, source='status.code')
    
    class Meta:
        model = Poem
        fields = ['id', 'parts']
        # exclude = ['created_at', 'updated_at']
