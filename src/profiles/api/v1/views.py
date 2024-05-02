from django.contrib.auth.models import User
from django.http import HttpResponseNotFound
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from rest_framework.response import Response
from rest_framework.views import APIView


from profiles.api.v1.serializers import FreelancerSerializer, CustomerSerializer
from profiles.models import Freelancer, Customer


class FreelancerDetailAPIView(APIView):
    def get(self, request, pk):
        freelancer = Freelancer.objects.filter(user__pk=pk)
        serializer = FreelancerSerializer(freelancer, many=True)
        return Response(serializer.data)


class CustomerDetailAPIView(APIView):
    def get(self, request, pk):
        customer = Customer.objects.filter(user__pk=pk)
        serializer = CustomerSerializer(customer, many=True)
        return Response(serializer.data)


class ProfileView(TemplateView):
    template_name = 'profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = kwargs.get('pk')
        context['freelancer'] = f'/api/v1/freelancer/{pk}/'
        context['customer'] = f'/api/v1/customer/{pk}/'
        return context


class HomeView(TemplateView):
    template_name = 'home.html'
