
from .models import Athlete
from rest_framework import serializers
from rest_framework.relations import HyperlinkedIdentityField, StringRelatedField
from rest_framework.serializers import HyperlinkedIdentityField


class AthleteSerializer(serializers.ModelSerializer):

    detail_url = HyperlinkedIdentityField( # link para abrir detalhes 
        view_name='athletes:atlhetes-detail',
        lookup_field='pk'
    )


    class Meta:
        model = Athlete
        fields = [

            'name',
            'sex',
            'height',
            'weight',
            'team',
            'detail_url',
            'events_count',
            'medals_count'
        ]


class AthleteDetailSerializer(serializers.ModelSerializer):

    athlete_events = StringRelatedField(many=True)

    class Meta:
        model = Athlete
        depth=1 # show foreign keys in detail
        fields = [
            'id',
            'name',
            'sex',
            'height',
            'weight',
            'team',
            'athlete_events', # comes from related name in events models
            'athlete_medals'# comes from related name in medals models
        ]