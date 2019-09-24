from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from books import views as books_views
from users import views as user_views

router = DefaultRouter()
router.register(r'books', books_views.BookViewSet)
router.register(r'users', user_views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]