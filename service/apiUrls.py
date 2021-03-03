from django.urls import path, include
from . import api


urlpatterns = [
    path('getresources/', api.getResources, name='getresources'),
]
