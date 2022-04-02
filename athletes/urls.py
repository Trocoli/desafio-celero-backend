from django.urls import include, path
from .views import AthletesListAPIView, AthletesRetrieveUpdateDestroyAPIView

app_name = "athletes"

urlpatterns = [
    path('list/', AthletesListAPIView.as_view(), name='athletes-list'),
    path('<int:pk>/', AthletesRetrieveUpdateDestroyAPIView.as_view(), name='atlhetes-detail')
]