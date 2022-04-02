from django.urls import include, path
from .views import OlympicsListAPIView, OlympicsRetrieveUpdateDestroyAPIView

app_name = "olympic-games"

urlpatterns = [
    path('list/', OlympicsListAPIView.as_view(), name='olympic-games-list'),
    path('<int:pk>/', OlympicsRetrieveUpdateDestroyAPIView.as_view(), name='olympics-detail')
]