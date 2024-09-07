from rest_framework import serializers

from customers.models import Customer


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'
        depth = 1


class CustomerCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['name', 'last_name', 'photo']

