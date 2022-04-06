from .models import Athlete
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import AthleteDetailSerializer, AthleteSerializer 
from rest_framework import filters 

from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    get_object_or_404) 


class AthletesListAPIView(ListCreateAPIView):

    queryset = Athlete.objects.all().order_by('-id') # lista todos os atletas ordenação por ordem alfabética 
    serializer_class = AthleteSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'height', 'weight', 'team',]

class AthletesRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):

    queryset = Athlete.objects.all()
    serializer_class = AthleteDetailSerializer
    lookup_field = 'pk'
