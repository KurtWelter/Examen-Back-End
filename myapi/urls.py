from django.urls import path, include
from rest_framework import routers
from .views import UsuarioViewSet, SesionViewSet, AlimentoMascotaViewSet, AlimentoPerroViewSet, AlimentoGatoViewSet
from .views import RegistroView

router = routers.DefaultRouter()
router.register(r'usuarios', UsuarioViewSet)
router.register(r'sesiones', SesionViewSet)
router.register(r'alimentos-mascotas', AlimentoMascotaViewSet)
router.register(r'alimentos-perros', AlimentoPerroViewSet)
router.register(r'alimentos-gatos', AlimentoGatoViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/registro', RegistroView.as_view(), name='registro'),
    # Other URL patterns for your project
]
