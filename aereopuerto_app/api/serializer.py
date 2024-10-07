from rest_framework import serializers
from aereopuerto_app.models import Pasajero, Equipaje, Aeropuerto, Terminal, Piloto, Copiloto, Sobrecargo, Avion, Avioneta, Helicoptero, Vuelo, Boleto

class PasajeroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pasajero
        fields = '__all__'

class EquipajeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipaje
        fields = '__all__'

class AeropuertoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aeropuerto
        fields = '__all__'

class TerminalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Terminal
        fields = '__all__'

class PilotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Piloto
        fields = '__all__'

class CopilotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Copiloto
        fields = '__all__'

class SobrecargoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sobrecargo
        fields = '__all__'

class AvionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Avion
        fields = '__all__'

class AvionetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Avioneta
        fields = '__all__'

class HelicopteroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Helicoptero
        fields = '__all__'

class VueloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vuelo
        fields = '__all__'

class BoletoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Boleto
        fields = '__all__'