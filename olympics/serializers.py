
from .models import Olympic
from rest_framework import serializers

class OlympicSerializer(serializers.ModelSerializer):

    class Meta:
        model = Olympic
        fields = [
            'year',
            'season',
            'city',
            # events 
        ]