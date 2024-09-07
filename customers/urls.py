from django.urls import path, include

from customers.routers import router


urlpatterns = [
    path('', include(router.urls)),
]