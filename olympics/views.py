from .models import Olympic
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import OlympicSerializer 

from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    get_object_or_404) 


class OlympicsListAPIView(ListCreateAPIView):

    queryset = Olympic.objects.all().order_by('-id')
    serializer_class = OlympicSerializer

class OlympicsRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):

    queryset = Olympic.objects.all()
    serializer_class = OlympicSerializer
    lookup_field = 'pk'
