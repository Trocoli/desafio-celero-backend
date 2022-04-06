from django.urls import include, path
from .views import AthletesListAPIView, AthletesRetrieveUpdateDestroyAPIView

app_name = "athletes"

urlpatterns = [
    path('', AthletesListAPIView.as_view(), name='athletes-list'), # lista de todos os atletas 
    path('<int:pk>/', AthletesRetrieveUpdateDestroyAPIView.as_view(), name='atlhetes-detail') # endpoint para edição, retrieve ou deleção 
]