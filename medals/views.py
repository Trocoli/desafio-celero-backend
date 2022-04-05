from .models import Medal
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import MedalSerializer

from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    RetrieveAPIView,
    get_object_or_404) 
from rest_framework import filters 


class MedalsListAPIView(ListCreateAPIView):

    queryset = Medal.objects.all().order_by('-id')
    serializer_class = MedalSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['medal_type']
    

class MedalRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView): # view no endpoint /medal/:id/ que permite métodos UPDATE, PATCH, DESTROY

    queryset = Medal.objects.all()
    serializer_class = MedalSerializer
    lookup_field = 'pk'
