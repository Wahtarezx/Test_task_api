from django.urls import path
from profiles.api.v1.views import FreelancerDetailAPIView, CustomerDetailAPIView, ProfileView, HomeView


urlpatterns = [
    path('freelancer/<int:pk>/', FreelancerDetailAPIView.as_view(), name='freelancer'),
    path('customer/<int:pk>/', CustomerDetailAPIView.as_view(), name='customers'),
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),
    path('home/', HomeView.as_view(), name='home'),
]
