from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from api.views import registrar_usuario
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # Esta es la URL de api.service.ts
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/register/', registrar_usuario),
    path('api/verify-email/', views.verificar_codigo),
]