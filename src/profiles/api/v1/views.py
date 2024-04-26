from rest_framework.response import Response
from rest_framework.views import APIView

from profiles.api.v1.serializers import FreelancerSerializer, CustomerSerializer
from profiles.models import Freelancer, Customer


class FreelancerDetailAPIView(APIView):
    def get(self, request, pk):
        freelancer = Freelancer.objects.filter(pk=pk)
        serializer = FreelancerSerializer(freelancer, many=True)
        return Response(serializer.data)


class CustomerDetailAPIView(APIView):
    def get(self, request, pk):
        customer = Customer.objects.filter(pk=pk)
        serializer = CustomerSerializer(customer, many=True)
        return Response(serializer.data)
