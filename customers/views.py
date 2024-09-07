from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from customers.models import Customer
from customers.serializers import CustomerSerializer, CustomerCreateSerializer


class AccountViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing Customers.
    """
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsAuthenticated, IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return CustomerSerializer
        if self.action in ['create', 'partial_update', 'update']:
            return CustomerCreateSerializer
        return CustomerSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)