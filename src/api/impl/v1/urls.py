from django.urls import include
from django.urls import path
from rest_framework.routers import DefaultRouter

from api.impl.v1.views import UserListViewSet


router = DefaultRouter()
router.register('users', UserListViewSet)

urlpatterns = [
    path("", include(router.urls)),
]