from rest_framework import routers

from users.views import UserViewSet
from customers.views import CostumerViewSet


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'customers', CostumerViewSet)