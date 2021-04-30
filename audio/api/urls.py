
from django.urls import path
from audio.api import views
from django.conf.urls import include
from rest_framework.routers import DefaultRouter

app_name = "audio"

api_router = DefaultRouter()
api_router.register('audio', views.AudioBookViewSet, 'audio-detail')

urlpatterns = [
    path('',include(api_router.urls)),
]