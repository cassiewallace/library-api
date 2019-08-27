from django.urls import path
from books import views


urlpatterns = [
    path('books/', views.BooksViewSet, name='books-all')
]