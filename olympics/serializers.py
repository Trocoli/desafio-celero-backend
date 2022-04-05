from .models import Olympic
from rest_framework import serializers


class OlympicSerializer(serializers.ModelSerializer):
    
    detail_url = serializers.HyperlinkedIdentityField( # link to detail view 
        view_name='olympic-games:olympics-detail',
        lookup_field='pk'
    )

    class Meta:
        model = Olympic
        fields = [
            'year',
            'season',
            'city',
            'detail_url'
            
        ]

class OlympicDetailSerializer(serializers.ModelSerializer):

        class Meta:
            depth = 1 # show events detail
            model = Olympic
            fields = [
                'year',
                'season',
                'city',
                'olympic_game', # relation to events

            
        ]