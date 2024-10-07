from rest_framework import viewsets
from aereopuerto_app.models import Pasajero, Equipaje, Aeropuerto, Terminal, Piloto, Copiloto, Sobrecargo, Avion, Avioneta, Helicoptero, Vuelo, Boleto
from aereopuerto_app.api.serializer import PasajeroSerializer, EquipajeSerializer, AeropuertoSerializer, TerminalSerializer, PilotoSerializer, CopilotoSerializer, SobrecargoSerializer, AvionSerializer, AvionetaSerializer, HelicopteroSerializer, VueloSerializer, BoletoSerializer

class PasajeroViewSet(viewsets.ModelViewSet):
    queryset = Pasajero.objects.all()
    serializer_class = PasajeroSerializer

class EquipajeViewSet(viewsets.ModelViewSet):
    queryset = Equipaje.objects.all()
    serializer_class = EquipajeSerializer

class AeropuertoViewSet(viewsets.ModelViewSet):
    queryset = Aeropuerto.objects.all()
    serializer_class = AeropuertoSerializer

class TerminalViewSet(viewsets.ModelViewSet):
    queryset = Terminal.objects.all()
    serializer_class = TerminalSerializer

class PilotoViewSet(viewsets.ModelViewSet):
    queryset = Piloto.objects.all()
    serializer_class = PilotoSerializer

class CopilotoViewSet(viewsets.ModelViewSet):
    queryset = Copiloto.objects.all()
    serializer_class = CopilotoSerializer

class SobrecargoViewSet(viewsets.ModelViewSet):
    queryset = Sobrecargo.objects.all()
    serializer_class = SobrecargoSerializer

class AvionViewSet(viewsets.ModelViewSet):
    queryset = Avion.objects.all()
    serializer_class = AvionSerializer

class AvionetaViewSet(viewsets.ModelViewSet):
    queryset = Avioneta.objects.all()
    serializer_class = AvionetaSerializer

class HelicopteroViewSet(viewsets.ModelViewSet):
    queryset = Helicoptero.objects.all()
    serializer_class = HelicopteroSerializer

class VueloViewSet(viewsets.ModelViewSet):
    queryset = Vuelo.objects.all()
    serializer_class = VueloSerializer

class BoletoViewSet(viewsets.ModelViewSet):
    queryset = Boleto.objects.all()
    serializer_class = BoletoSerializer