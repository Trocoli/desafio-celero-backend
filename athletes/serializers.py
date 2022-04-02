from .models import Athlete
from rest_framework import serializers
from rest_framework.relations import HyperlinkedIdentityField, StringRelatedField

# Todo 
# Add detail serializer 

class AthleteSerializer(serializers.ModelSerializer):

    detail_url = HyperlinkedIdentityField( # link para abrir detalhes e editar ou excluir atleta
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
            # events , 
            # medals , 
        ]