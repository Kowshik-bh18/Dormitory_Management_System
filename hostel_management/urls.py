from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path,include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('admission.urls')),
    path('hoste/',include('hostel.urls')),
    path('timetable',include('timetable.urls')),
    path('chatrooms/',include('chatroom.urls')),
    path('profile/',include('userprofile.urls')),
    path("chatbot/", include("chatbot.urls")),
]

if(settings.DEBUG):
    urlpatterns +=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)