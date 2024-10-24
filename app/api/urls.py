from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UsuarioViewSet, MateriaViewSet, NotaViewSet

router = DefaultRouter()
router.register(r'usuarios', UsuarioViewSet)
router.register(r'materias', MateriaViewSet)
router.register(r'notas', NotaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns += [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
