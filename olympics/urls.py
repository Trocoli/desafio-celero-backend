from django.urls import include, path
from .views import OlympicsListAPIView, OlympicRetrieveUpdateDestroyAPIView, OlympicDetail

app_name = "olympic-games"

# paths para /olympics/ 
urlpatterns = [
    path('', OlympicsListAPIView.as_view(), name='olympic-games-list'), # list all and allow POST
    path('update/<int:pk>/', OlympicRetrieveUpdateDestroyAPIView.as_view(), name='olympics-update-destroy'), # get by id and allows PATCH UPDATE and DESTROY methods
    path('<int:pk>/', OlympicDetail.as_view(), name='olympics-detail') # get by id to show details 
]