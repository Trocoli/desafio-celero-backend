from .models import Event
from athletes.models import Athlete
from rest_framework import serializers
from rest_framework.serializers import (
    ModelSerializer,
    HyperlinkedIdentityField,
    SerializerMethodField
)
from athletes.serializers import AthleteSerializer
from olympics.serializers import OlympicSerializer


class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = [
            'event_name',
            'sport_name',
            'athletes',
            'olympic_game'
        ]

class EventDetailSerializer(serializers.ModelSerializer):

    athletes = AthleteSerializer(many=True, read_only=True )
    olympic_game = OlympicSerializer( read_only=True)
    # medals 

    class Meta:
        model = Event
        fields = [
            'event_name',
            'sport_name',
            'athletes',
            'olympic_game'
            # olympics related? add on models needed
            # events 
        ]