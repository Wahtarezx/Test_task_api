from django.urls import path
from profiles.api.v1.views import FreelancerDetailAPIView, CustomerDetailAPIView


urlpatterns = [
    path('freelancer/<int:pk>/', FreelancerDetailAPIView.as_view(), name='freelancer'),
    path('customer/<int:pk>/', CustomerDetailAPIView.as_view(), name='customers'),
]
