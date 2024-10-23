from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('admission.urls')),
    path('hoste/',include('hostel.urls')),
    path('timetable',include('timetable.urls')),
    path('reports/',include('reports.urls')),
    path('announcment/',include('announcment')),
]
