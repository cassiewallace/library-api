from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from books import views as books_views
from users import views as user_views

router = routers.DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('', include('books.urls')),
    path('', include('users.urls')),
    path('auth/', include('rest_framework.urls', namespace='rest_framework'))
]
