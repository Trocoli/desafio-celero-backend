from pyexpat import model

from medals.models import Medal
from events.models import Event
from medals.serializers import MedalSerializer
from .models import Athlete
from rest_framework import serializers
from rest_framework.relations import HyperlinkedIdentityField, StringRelatedField


from rest_framework.serializers import (
    ModelSerializer,
    HyperlinkedIdentityField,
    SerializerMethodField
)


class AthleteSerializer(serializers.ModelSerializer):

    detail_url = HyperlinkedIdentityField( # link para abrir detalhes e editar ou excluir atleta
        view_name='athletes:atlhetes-detail',
        lookup_field='pk'
    )


    #medal_count = SerializerMethodField()
    events_count = SerializerMethodField()

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
#    def get_medal_count(self, obj):   #  contador de postagens e usuários por grupos. abrir detalhes para visualizar  
 #       count =  Medal.objects.filter(athlete = obj.id).count()
  #      return count
    
    def get_events_count(self, obj):
        count = Event.objects.filter(athletes = obj.id).count()
        return count

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