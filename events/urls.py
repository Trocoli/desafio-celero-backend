from django.urls import include, path
from .views import EventDetail, EventsListAPIView, EventRetrieveUpdateDestroyAPIView

app_name = "event"

urlpatterns = [
    path('list/', EventsListAPIView.as_view(), name='events-list'),
    path('update/<int:pk>/', EventRetrieveUpdateDestroyAPIView.as_view(), name='event-update-destroy'),
    path('<int:pk>/', EventDetail.as_view(), name='event-detail')
]