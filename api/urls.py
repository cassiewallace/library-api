from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from books import views as books_views
from users import views as user_views

router = routers.DefaultRouter()

urlpatterns = [
    # Note: it's currently only using the first path here to display in the admin.
    # This is going to be fixed when we use routers in Tutorial 6, so leaving it for now.
    path('', user_views.api_root),
    path('', books_views.api_root),
    path('', include(router.urls)),
    path('', include('books.urls')),
    path('', include('users.urls')),
    path('auth/', include('rest_framework.urls', namespace='rest_framework'))
]
