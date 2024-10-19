from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),  # Django admin panel
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # JWT token access
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # JWT token refresh
    path('api/', include('products.urls')), 
    path('api/accounts/', include('accounts.urls')),  # Ajoutez cette ligne
]
