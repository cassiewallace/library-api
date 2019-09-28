from django.contrib import admin, auth
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from books import views as books_views
from users import views as user_views

router = DefaultRouter()
router.register('books', books_views.BookViewSet)
router.register('users', user_views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
]