
from django.contrib import admin
from django.urls import include, path
from populate_app.views import upload_data

urlpatterns = [
    path('admin/', admin.site.urls),
    path('athletes/' , include('athletes.urls', namespace='athletes' )),
    path('olympics/' , include('olympics.urls', namespace='olympic-games' )),
    path('events/', include('events.urls', namespace='events' )),
    path('medals/', include('medals.urls', namespace='medals' )),

    path('populate/', upload_data)
]
