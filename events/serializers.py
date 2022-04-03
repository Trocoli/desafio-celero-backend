from .models import Event
from athletes.models import Athlete
from rest_framework import serializers
from rest_framework.relations import HyperlinkedIdentityField, StringRelatedField
from rest_framework.serializers import (
    ModelSerializer,
    HyperlinkedIdentityField,
    SerializerMethodField
)
from athletes.serializers import AthleteSerializer
from olympics.serializers import OlympicSerializer


class EventSerializer(serializers.ModelSerializer):

    detail_url = HyperlinkedIdentityField( # link para abrir detalhes e editar ou excluir atleta
        view_name='event:event-detail',
        lookup_field='pk'
    )

    winners = StringRelatedField(many=True)

    class Meta:
        model = Event
        fields = [
            'event_name',
            'sport_name',
            'athletes',
            'olympic_game',
            'detail_url',
            'winners'
        ]

class EventDetailSerializer(serializers.ModelSerializer):

    athletes = AthleteSerializer(many=True, read_only=True )
    olympic_game = OlympicSerializer( read_only=True)
    

    class Meta:
        depth= 1
        model = Event
        fields = [
            'event_name',
            'sport_name',
            'athletes',
            'olympic_game',
            'winners'
            # olympics related? add on models needed
            # events 
        ]