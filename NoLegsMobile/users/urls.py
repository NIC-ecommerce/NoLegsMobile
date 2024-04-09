from django.urls import path
from .views import *

urlpatterns = [
    path('users/create/', CustomUserCreateView.as_view(), name='user-create'),
    path('users/', CustomUserListView.as_view(), name='user-list'),
    path('users/<int:pk>/', CustomUserRetrieveUpdateDestroyView.as_view(), name='user-detail'),
    path('registration/', CustomUserRegistrationView.as_view(), name='user-registration'),
    path('login/', CustomUserLoginView.as_view(), name='user-login'),
    path('logout/', CustomUserLogoutView.as_view(), name='user-logout'),
]
