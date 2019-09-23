from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from users import views


urlpatterns = [
    path('users/', views.UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', views.UserDetail.as_view(), name='user-view')
]

urlpatterns = format_suffix_patterns(urlpatterns)