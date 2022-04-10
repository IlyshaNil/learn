from django.conf import settings
from django.urls import include
from django.urls import path
from django.urls import re_path


urlpatterns = [
    path("", include("api.impl.urls")),
]