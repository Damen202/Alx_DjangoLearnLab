from django.contrib import admin
from django.urls import path, include
from api.views import BookViewsets
from rest_framework import routers

# Router instance
router = routers.DefaultRouter()
router.register(r'books', BookViewsets, basename='book')  # simpler name

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),  # includes all CRUD endpoints
]
