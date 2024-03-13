from .views import SignupView, ProfileView, UpdateProfileView
from django.urls import path, include

app_name='accounts'
urlpatterns = [
    path('signup', SignupView.as_view(), name='signup'),
    path('profile/<str:username>', ProfileView.as_view(), name='profile'),
    path('update', UpdateProfileView.as_view(), name='profile-update'),
]