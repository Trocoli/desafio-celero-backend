from .models import Olympic
from .serializers import OlympicDetailSerializer, OlympicSerializer 

from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    RetrieveAPIView,
    get_object_or_404) 
from rest_framework import filters


class OlympicsListAPIView(ListCreateAPIView):

    queryset = Olympic.objects.all().order_by('-year')
    serializer_class = OlympicSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['city', 'year']

class OlympicRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView): # View que permite os metodos update patch e delete no endpoint /olympic/update/:id

    queryset = Olympic.objects.all()
    serializer_class = OlympicSerializer
    lookup_field = 'pk'



class OlympicDetail(RetrieveAPIView):
    queryset = Olympic.objects.all()
    serializer_class = OlympicDetailSerializer
    lookup_field = 'pk'
