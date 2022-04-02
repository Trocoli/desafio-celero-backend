from django.urls import include, path
from .views import EventsListAPIView, EventRetrieveUpdateDestroyAPIView

app_name = "event"

urlpatterns = [
    path('list/', EventsListAPIView.as_view(), name='events-list'),
    path('<int:pk>/', EventRetrieveUpdateDestroyAPIView.as_view(), name='event-detail')
]