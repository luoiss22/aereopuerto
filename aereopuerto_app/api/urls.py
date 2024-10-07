from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PasajeroViewSet, EquipajeViewSet, AeropuertoViewSet, TerminalViewSet, PilotoViewSet, CopilotoViewSet, SobrecargoViewSet, AvionViewSet, AvionetaViewSet, HelicopteroViewSet, VueloViewSet, BoletoViewSet

router = DefaultRouter()
router.register(r'pasajeros', PasajeroViewSet)
router.register(r'equipajes', EquipajeViewSet)
router.register(r'aeropuertos', AeropuertoViewSet)
router.register(r'terminales', TerminalViewSet)
router.register(r'pilotos', PilotoViewSet)
router.register(r'copilotos', CopilotoViewSet)
router.register(r'sobrecargos', SobrecargoViewSet)
router.register(r'aviones', AvionViewSet)
router.register(r'avionetas', AvionetaViewSet)
router.register(r'helicopteros', HelicopteroViewSet)
router.register(r'vuelos', VueloViewSet)
router.register(r'boletos', BoletoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]