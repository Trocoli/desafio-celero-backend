from django.urls import include, path
from .views import MedalsListAPIView, MedalRetrieveUpdateDestroyAPIView

app_name = "medals"

urlpatterns = [
    path('', MedalsListAPIView.as_view(), name='medals-list'),
    path('<int:pk>/', MedalRetrieveUpdateDestroyAPIView.as_view(), name='medal-detail')
]