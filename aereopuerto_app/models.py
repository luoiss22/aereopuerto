from django.db import models

# Create your models here.

class Persona(models.Model):  # Convertir en una clase base normal
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=255)  # Dirección
    apellido = models.CharField(max_length=100)
    fecha_nac = models.DateField()  # Fecha de nacimiento
    discapacidad = models.BooleanField(default=False)  # Discapacidad (sí o no)

    def viajar(self):
        pass

    def comer(self):
        pass

    def dormir(self):
        pass

    def abordar(self):
        pass

    def check_in(self):
        pass

    def irBanio(self):
        pass


class Pasajero(Persona):
    idPasajero = models.AutoField(primary_key=True)
    nacionalidad = models.CharField(max_length=50)

    def __str__(self):
        return f"Pasajero {self.nombre} {self.apellido} - ID: {self.idPasajero}"

    def comer(self):
        print(f"{self.nombre} {self.apellido} está comiendo.")

    def dormir(self):
        print(f"{self.nombre} {self.apellido} está durmiendo.")

    def abordar(self):
        print(f"{self.nombre} {self.apellido} está abordando el avión.")

    def check_in(self):
        print(f"{self.nombre} {self.apellido} está haciendo check-in.")

    def irBanio(self):
        print(f"{self.nombre} {self.apellido} está yendo al baño.")


class Equipaje(models.Model):
    idEquipaje = models.AutoField(primary_key=True)
    peso = models.CharField(max_length=50)  # En kilogramos
    altura = models.CharField(max_length=50)  # En centímetros
    tipo = models.CharField(max_length=50)  # Ejemplo: "maleta", "mochila", etc.
    idPasajero = models.ForeignKey(Pasajero, on_delete=models.CASCADE, related_name='equipajes')

    def __str__(self):
        return f"Equipaje de {self.idPasajero}: {self.tipo} - {self.peso} kg"


class Aeropuerto(models.Model):
    idAeropuerto = models.AutoField(primary_key=True)
    nombreAeropuerto = models.CharField(max_length=255)
    numPistas = models.IntegerField()
    tipoAvion = models.CharField(max_length=255)

    def __str__(self):
        return f"Aeropuerto {self.nombreAeropuerto} - ID: {self.idAeropuerto}"


class Terminal(models.Model):
    idTerminal = models.AutoField(primary_key=True)
    capacidad = models.IntegerField()
    disponible = models.BooleanField()
    idAeropuerto = models.OneToOneField(Aeropuerto, on_delete=models.CASCADE, related_name='terminal')

    def __str__(self):
        return f"Terminal {self.idTerminal} - Capacidad: {self.capacidad}"


class Tripulacion(Persona):  # Subclase de Persona
    idTripulacion = models.AutoField(primary_key=True)
    antiguedad = models.IntegerField()
    turno = models.CharField(max_length=50)
    horasVuelo = models.FloatField()
    genero = models.CharField(max_length=10)
    idVuelo = models.ForeignKey('Vuelo', on_delete=models.CASCADE, related_name='tripulacion')

    def __str__(self):
        return f"Tripulación {self.nombre} - ID: {self.idTripulacion}"

    def viajar(self):
        print(f"{self.nombre} está viajando como tripulante.")

    def comer(self):
        print(f"{self.nombre} está comiendo.")

    def dormir(self):
        print(f"{self.nombre} está durmiendo.")

    def abordar(self):
        print(f"{self.nombre} está abordando el avión.")

    def check_in(self):
        print(f"{self.nombre} está haciendo check-in.")

    def irBanio(self):
        print(f"{self.nombre} está yendo al baño.")


class Piloto(Tripulacion):  # Subclase de Tripulacion
    idPiloto = models.AutoField(primary_key=True)
    rango = models.CharField(max_length=50)
    licencia = models.CharField(max_length=50)
    tipoAeronave = models.CharField(max_length=50)
    saludMental = models.CharField(max_length=50)
    tripulacion_ref = models.OneToOneField(Tripulacion, on_delete=models.CASCADE, related_name='piloto_tripulacion')

    def __str__(self):
        return f"Piloto: {self.idPiloto} - Rango: {self.rango}"


class Copiloto(Tripulacion):  # Subclase de Tripulacion
    idCopiloto = models.AutoField(primary_key=True)
    rango = models.CharField(max_length=50)
    tiempoRestantePiloto = models.TimeField()
    tripulacion_ref = models.OneToOneField(Tripulacion, on_delete=models.CASCADE, related_name='copiloto_tripulacion')

    def __str__(self):
        return f"Copiloto: {self.idCopiloto} - Rango: {self.rango}"


class Sobrecargo(Tripulacion):  # Subclase de Tripulacion
    idSobrecargo = models.AutoField(primary_key=True)
    idiomas = models.CharField(max_length=255)
    certificados = models.CharField(max_length=255)
    tripulacion_ref = models.OneToOneField(Tripulacion, on_delete=models.CASCADE, related_name='sobrecargo_tripulacion')

    def __str__(self):
        return f"Sobrecargo: {self.idSobrecargo} - Idiomas: {self.idiomas}"


class VehiculoAereo(models.Model):
    idVehiculoAereo = models.AutoField(primary_key=True)
    matricula = models.CharField(max_length=50, unique=True)
    serie = models.CharField(max_length=100)
    capacidad = models.IntegerField()
    color = models.CharField(max_length=50)
    estado = models.BooleanField()
    antiguedad = models.CharField(max_length=50)
    tiempoAire = models.FloatField()
    llantas = models.IntegerField()
    tanque = models.CharField(max_length=50)
    distancia = models.FloatField()

    def __str__(self):
        return f"Vehículo Aéreo {self.matricula} - Serie: {self.serie}"


class Avion(VehiculoAereo):  # Subclase de VehiculoAereo
    idAvion = models.AutoField(primary_key=True)
    aerolinea = models.CharField(max_length=100)
    tipoMotor = models.CharField(max_length=100)
    puertas = models.IntegerField()
    tipoAvion = models.CharField(max_length=50)
    vehiculo_aereo = models.OneToOneField(VehiculoAereo, on_delete=models.CASCADE, related_name='avion_vehiculo_aereo')

    def __str__(self):
        return f"Avión {self.idAvion} - Aerolínea: {self.aerolinea}"


class Avioneta(VehiculoAereo):  # Subclase de VehiculoAereo
    idAvioneta = models.AutoField(primary_key=True)
    numeroMotores = models.IntegerField()
    tipoPista = models.CharField(max_length=255)
    clasificacion = models.CharField(max_length=50)
    tipoConcesion = models.CharField(max_length=50)
    vehiculo_aereo = models.OneToOneField(VehiculoAereo, on_delete=models.CASCADE, related_name='avioneta_vehiculo_aereo')

    def __str__(self):
        return f"Avioneta {self.idAvioneta} - Clasificación: {self.clasificacion}"


class Helicoptero(VehiculoAereo):  # Subclase de VehiculoAereo
    idHelicoptero = models.AutoField(primary_key=True)
    numeroHelices = models.IntegerField()
    tipoHelicoptero = models.CharField(max_length=50)
    vehiculo_aereo = models.OneToOneField(VehiculoAereo, on_delete=models.CASCADE, related_name='helicoptero_vehiculo_aereo')

    def __str__(self):
        return f"Helicóptero {self.idHelicoptero} - Tipo: {self.tipoHelicoptero}"


class Vuelo(models.Model):
    idVuelo = models.AutoField(primary_key=True)
    origen = models.CharField(max_length=100)
    destino = models.CharField(max_length=100)
    duracion = models.TimeField()
    horaSalida = models.CharField(max_length=50)
    horaLlegada = models.CharField(max_length=50)
    idVehiculoAereo = models.OneToOneField(VehiculoAereo, on_delete=models.CASCADE, related_name='vuelo')
    idTerminal = models.OneToOneField(Terminal, on_delete=models.CASCADE, related_name='vuelo')

    def __str__(self):
        return f"Vuelo {self.idVuelo} - De {self.origen} a {self.destino}"


class Boleto(models.Model):  # Modelo de Boleto
    idBoleto = models.AutoField(primary_key=True)
    asiento = models.CharField(max_length=20)
    costo = models.DecimalField(max_digits=10, decimal_places=2)
    idPasajero = models.OneToOneField(Pasajero, on_delete=models.CASCADE, related_name='boleto')
    idVuelo = models.OneToOneField(Vuelo, on_delete=models.CASCADE, related_name='boleto')

    def __str__(self):
        return f"Boleto para {self.idPasajero.nombre} en el vuelo {self.idVuelo} - Asiento: {self.asiento}"