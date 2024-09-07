from oauth2_provider import urls as oauth2_urls
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include(oauth2_urls)),
    path('api/', include('rest_framework.urls')),
    path('api/', include('customers.urls')),

]
