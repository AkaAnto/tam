from rest_framework import routers

from customers.views import AccountViewSet


router = routers.SimpleRouter()
router.register(r'customers', AccountViewSet)