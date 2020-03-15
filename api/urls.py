from django.urls import path, include

from.views import apiTest

urlpatterns = [
    path('api-test/', apiTest),
]