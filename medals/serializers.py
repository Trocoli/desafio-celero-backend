from .models import Medal
from rest_framework import serializers
from rest_framework.serializers import (
    ModelSerializer,
    HyperlinkedIdentityField,
    SerializerMethodField
)

class MedalSerializer(serializers.ModelSerializer):
    detail_url = HyperlinkedIdentityField( # link para abrir detalhes e editar ou excluir atleta
        view_name='medals:medal-detail',
        lookup_field='pk'
    )

    class Meta:
        model = Medal
        depth = 1
        fields = [
            'event_name',
            'olympic_game',
            'athlete',
            'medal_type',
            'detail_url'
        ]
