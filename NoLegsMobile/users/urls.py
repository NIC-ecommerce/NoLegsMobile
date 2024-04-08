from django.urls import path
from .views import CustomUserCreateView, CustomUserListView, CustomUserRetrieveUpdateDestroyView

urlpatterns = [
    path('users/create/', CustomUserCreateView.as_view(), name='user-create'),
    path('users/', CustomUserListView.as_view(), name='user-list'),
    path('users/<int:pk>/', CustomUserRetrieveUpdateDestroyView.as_view(), name='user-detail'),
]
