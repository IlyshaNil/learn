from django.urls import include
from django.urls import path

urlpatterns = [path("v1/", include("api.impl.v1.urls"))]