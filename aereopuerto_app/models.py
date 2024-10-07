from django.db import models

# Create your models here.

class Persona(models.Model):  # Convertir en una clase base normal
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=255)  # Dirección
    apellido = models.CharField(max_length=100)
    fecha_nac = models.DateField()  # Fecha de nacimiento
    discapacidad = models.BooleanField(default=False)  # Discapacidad (sí o no)

    class Meta:
        abstract = True  # Hace que Persona sea un modelo abstracto

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


class Pasajero(Persona):  # Hereda de Persona
    def viajar(self):
        # Implementación del método
        print(f"{self.nombre} está viajando.")

    def comer(self):
        # Implementación del método
        print(f"{self.nombre} está comiendo.")

    def dormir(self):
        # Implementación del método
        print(f"{self.nombre} está durmiendo.")

    def abordar(self):
        # Implementación del método
        print(f"{self.nombre} está abordando el avión.")

    def check_in(self):
        # Implementación del método
        print(f"{self.nombre} está haciendo check-in.")

    def irBanio(self):
        # Implementación del método
        print(f"{self.nombre} está yendo al baño.")

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Equipaje(models.Model):
    peso = models.FloatField()  # En kilogramos
    altura = models.FloatField()  # En centímetros
    ancho = models.FloatField()  # En centímetros
    pasajero = models.ForeignKey(Pasajero, on_delete=models.CASCADE, related_name='equipajes')  # Relación con Pasajero
    tipo = models.CharField(max_length=50)  # Ejemplo: "maleta", "mochila", etc.

    def __str__(self):
        return f"Equipaje de {self.pasajero}: {self.tipo} - {self.peso} kg"


class Aeropuerto(models.Model):
    clave_aeropuerto = models.CharField(max_length=10, unique=True)  # Clave única para el aeropuerto
    nombre = models.CharField(max_length=100)  # Nombre del aeropuerto
    numero_pistas = models.IntegerField()  # Número de pistas disponibles
    tipo_avion = models.CharField(max_length=50)  # Tipo de avión operado (ejemplo: "comercial", "privado", etc.)

    def __str__(self):
        return self.nombre


class Terminal(models.Model):
    clave_terminal = models.CharField(max_length=10, unique=True)  # Clave única para la terminal
    capacidad = models.IntegerField()  # Capacidad máxima de la terminal
    disponible = models.BooleanField(default=True)  # Disponibilidad (sí o no)
    aeropuerto = models.ForeignKey(Aeropuerto, on_delete=models.CASCADE, related_name='terminales')  # Relación con Aeropuerto

    def __str__(self):
        return f"Terminal {self.clave_terminal} en {self.aeropuerto.nombre}"


class Tripulacion(Persona):  # Modelo padre
    codigo = models.CharField(max_length=20, unique=True)
    antiguedad = models.IntegerField()
    turno = models.CharField(max_length=20)
    horasVuelo = models.FloatField()
    genero = models.CharField(max_length=10)

    class Meta:
        abstract = True  # Hace que Tripulacion sea un modelo abstracto

    def viajar(self):
        print(f"{self.nombre} {self.apellido} está viajando como tripulante.")

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

    def __str__(self):
        return f"{self.nombre} {self.apellido} (Código: {self.codigo})"


class Piloto(Tripulacion):  # Subclase de Tripulacion
    rango = models.CharField(max_length=50)  # Ejemplo de atributo específico para Piloto
    horas = models.FloatField()  # Horas de vuelo acumuladas
    tipo_aeronave = models.CharField(max_length=50)  # Tipo de aeronave que pilota
    salud_mental = models.CharField(max_length=50)  # Estado de salud mental

    def __str__(self):
        return f"Piloto: {self.nombre} {self.apellido}, Rango: {self.rango}"


class Copiloto(Tripulacion):  # Subclase de Tripulacion
    rango = models.CharField(max_length=50)  # Rango del copiloto
    tiempo_restante = models.IntegerField()  # Tiempo restante para convertirse en capitán (en días)

    def __str__(self):
        return f"Copiloto: {self.nombre} {self.apellido}, Rango: {self.rango}"


class Sobrecargo(Tripulacion):  # Subclase de Tripulacion
    idiomas = models.CharField(max_length=100)  # Idiomas que habla el sobrecargo
    certificados = models.CharField(max_length=255)  # Certificados que posee

    def __str__(self):
        return f"Sobrecargo: {self.nombre} {self.apellido}, Idiomas: {self.idiomas}"


class VehiculoAereo(models.Model):  # Modelo padre
    matricula = models.CharField(max_length=50, unique=True)
    modelo = models.CharField(max_length=100)
    serie = models.CharField(max_length=100)
    capacidad = models.IntegerField()
    color = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)  # Estado del vehículo (activo, en mantenimiento, etc.)
    antiguedad = models.IntegerField()  # Antigüedad en años

    class Meta:
        abstract = True  # Hace que VehiculoAereo sea un modelo abstracto

    def __str__(self):
        return f"Vehículo Aéreo {self.modelo} - Matrícula: {self.matricula}"


class Avion(VehiculoAereo):  # Subclase de VehiculoAereo
    aerolinea = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50)  # Tipo de avión (comercial, carga, etc.)
    motor = models.CharField(max_length=100)
    puertas = models.IntegerField()

    def __str__(self):
        return f"Avión {self.modelo} - Aerolínea: {self.aerolinea}"


class Avioneta(VehiculoAereo):  # Subclase de VehiculoAereo
    especificacion = models.CharField(max_length=255)  # Especificaciones adicionales
    clasificacion = models.CharField(max_length=50)  # Clasificación de la avioneta
    numeroMotores = models.IntegerField()

    def __str__(self):
        return f"Avioneta {self.modelo} - Clasificación: {self.clasificacion}"


class Helicoptero(VehiculoAereo):  # Subclase de VehiculoAereo
    helices = models.IntegerField()  # Número de hélices
    tipo = models.CharField(max_length=50)  # Tipo de helicóptero (rescate, militar, etc.)

    def __str__(self):
        return f"Helicóptero {self.modelo} - Tipo: {self.tipo}"


class Vuelo(models.Model):
    vehiculoAereo = models.ForeignKey(Avion, on_delete=models.CASCADE)  # Relación con Avion
    origen = models.CharField(max_length=100)
    destino = models.CharField(max_length=100)
    piloto = models.ForeignKey(Piloto, on_delete=models.CASCADE)  # Relación con Piloto
    copiloto = models.ForeignKey(Copiloto, on_delete=models.CASCADE)  # Relación con Copiloto
    sobrecargos = models.ManyToManyField(Sobrecargo)  # Relación con Sobrecargos
    terminal = models.ForeignKey(Terminal, on_delete=models.CASCADE)
    duracion = models.DurationField()
    horaSalida = models.DateTimeField()
    horaDestino = models.DateTimeField()

    def __str__(self):
        return f"Vuelo de {self.origen} a {self.destino} - Vehículo: {self.vehiculoAereo}"


class Boleto(models.Model):  # Modelo de Boleto
    pasajero = models.ForeignKey(Pasajero, on_delete=models.CASCADE)  # Relación con Pasajero
    vuelo = models.ForeignKey(Vuelo, on_delete=models.CASCADE)  # Relación con Vuelo
    asiento = models.CharField(max_length=20)  # Número de asiento
    costo = models.DecimalField(max_digits=10, decimal_places=2)  # Costo del boleto

    def __str__(self):
        return f"Boleto para {self.pasajero.nombre} en el vuelo {self.vuelo} - Asiento: {self.asiento}"