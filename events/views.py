from .models import Event
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import EventSerializer, EventDetailSerializer

from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    get_object_or_404) 


class EventsListAPIView(ListCreateAPIView):

    queryset = Event.objects.all().order_by('-id')
    serializer_class = EventSerializer

class EventRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):

    queryset = Event.objects.all()
    serializer_class = EventDetailSerializer
    lookup_field = 'pk'
