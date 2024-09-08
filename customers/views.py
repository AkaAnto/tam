from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from customers.models import Customer
from customers.serializers import CustomerSerializer, CustomerCreateUpdateSerializer


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
            return CustomerCreateUpdateSerializer
        return CustomerSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(author=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        print(f'Data {request.data}')
        serializer = self.get_serializer(data=request.data, instance=self.get_object())
        if serializer.is_valid(raise_exception=True):
            serializer.save(editor=request.user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)