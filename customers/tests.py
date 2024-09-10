from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model

from customers.models import Customer


class APITests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='user',
            password='password'
        )
        self.admin_user = get_user_model().objects.create_user(
            username='admin',
            password='admin',
            is_superuser=True,
            is_staff=True,
        )
        self.customer = Customer.objects.create(
            author=self.user,
            name='John',
            last_name='Doe',
        )
        self.token = RefreshToken.for_user(self.user).access_token
        self.admin_token = RefreshToken.for_user(self.admin_user).access_token
        self.client = APIClient()

    def test_customer_endpoint_jwt(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + str(self.token))
        response = self.client.get('/api/customers/')
        self.assertEqual(response.status_code, 200)
        response_data = response.data.get('results', [])[0]
        self.assertEqual(response_data.get('name', 'unset'), 'John')

    def test_customer_endpoint_no_jwt(self):
        response = self.client.get('/api/customers/')
        self.assertEqual(response.status_code, 401)

    def test_user_endpoint_admin(self):
        print(str(self.admin_token))
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + str(self.admin_token))
        response = self.client.get('/api/users/')
        self.assertEqual(response.status_code, 200)

    def test_user_endpoint_not_admin(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + str(self.token))
        response = self.client.get('/api/users/')
        self.assertEqual(response.status_code, 403)