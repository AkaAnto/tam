from rest_framework import serializers

from customers.models import Customer
from users.models import User


class RelatedUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'username', 'is_superuser']


class CustomerSerializer(serializers.ModelSerializer):
    author = RelatedUserSerializer(read_only=True)
    editor = RelatedUserSerializer(read_only=True)
    class Meta:
        model = Customer
        fields = '__all__'


class CustomerCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['name', 'last_name', 'photo']

