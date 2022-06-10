from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from books.views import UserViewSet

router = routers.DefaultRouter()
router.register('user', UserViewSet, basename='Users')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
