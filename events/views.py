from rest_framework import filters 
from .models import Event
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import EventSerializer, EventDetailSerializer

from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    RetrieveAPIView,
    get_object_or_404) 


class EventsListAPIView(ListCreateAPIView):

    queryset = Event.objects.all().order_by('-id')
    serializer_class = EventSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['event_name', 'sport_name']

class EventRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):

    queryset = Event.objects.all()
    serializer_class = EventSerializer
    lookup_field = 'pk'


class EventDetail(RetrieveAPIView):
    queryset = Event.objects.all()
    serializer_class = EventDetailSerializer
    lookup_field = 'pk'

