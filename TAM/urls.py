from django.conf.urls.static import static
from oauth2_provider import urls as oauth2_urls
from rest_framework_simplejwt import views as jwt_views
from django.contrib import admin
from django.urls import path, include

from TAM import settings
from TAM.api_routes import router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include(oauth2_urls)),
    path('api/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
