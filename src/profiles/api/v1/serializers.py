from rest_framework import serializers
from profiles.models import Customer, Freelancer, Review
from django.contrib.auth.models import User


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'pk', 'user', 'text'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['pk', 'username', 'email', 'first_name', 'last_name',]


class FreelancerSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    review = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Freelancer
        fields = [
            'pk', 'user', 'cost_of_work', 'experience', 'contact_phone',
            'ownership_form', 'payment_method', 'about_me', 'portfolio',
            'image', 'review',
        ]


class CustomerSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    review = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Customer
        fields = [
            'pk', 'user', 'payment', 'experience', 'contact_phone',
            'ownership_form', 'about_us', 'logo', 'review'
        ]
