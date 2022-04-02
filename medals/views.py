from .models import Medal
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import MedalSerializer

from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    get_object_or_404) 


class MedalsListAPIView(ListCreateAPIView):

    queryset = Medal.objects.all().order_by('-id')
    serializer_class = MedalSerializer

class MedalRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):

    queryset = Medal.objects.all()
    serializer_class = MedalSerializer
    lookup_field = 'pk'
