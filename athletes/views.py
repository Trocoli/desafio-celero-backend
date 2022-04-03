from .models import Athlete
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import AthleteDetailSerializer, AthleteSerializer 

from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    get_object_or_404) 


class AthletesListAPIView(ListCreateAPIView):

    queryset = Athlete.objects.all().order_by('-id')
    serializer_class = AthleteSerializer

class AthletesRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):

    queryset = Athlete.objects.all()
    serializer_class = AthleteDetailSerializer
    lookup_field = 'pk'
