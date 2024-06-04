from enum import Enum

from django.db import models

class Persona(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    dni = models.CharField(max_length=8, unique=True)
    email = models.EmailField()

    class Meta:
        abstract = True

class Cliente(Persona):
    telefono = models.CharField(max_length=10)

    def pedirHabitacion(self):
        pass

    def darInformacion(self):
        pass

class Empleado(Persona):
    cargo = models.CharField(max_length=50)

    def asignarHabitacion(self):
        pass

    def verificarEstado(self):
        pass

class TipoHabitacion(Enum):
    SIMPLE = 'Simple'
    DOBLE = 'Doble'
    SUITE = 'Suite'

class Habitacion(models.Model):
    numero = models.IntegerField()
    tipo = models.CharField(max_length=10, choices=[(tag, tag.value) for tag in TipoHabitacion])
    precio = models.FloatField()

    def verificarEstado(self):
        pass

    def reservar(self):
        pass

class EstadoReserva(Enum):
    RESERVADA = 'Reservada'
    OCUAPDA = 'Ocupada'
    LIBRE = 'Libre'

class Reservacion(models.Model):
    codigo = models.CharField(max_length=10, unique=True)
    fecha_inicio = models.DateField()
    estado = models.CharField(max_length=10, choices=[(tag, tag.value) for tag in EstadoReserva])
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='reservacionList')
    habitacion = models.ForeignKey(Habitacion, on_delete=models.CASCADE)

    def realizarReserva(self):
        pass

    def cancelarReserva(self):
        pass

    def reagendarReserva(self):
        pass

class Factura(models.Model):
    numeroFactura = models.CharField(max_length=10, unique=True)
    fecha = models.DateField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    valorTotal = models.FloatField()
    descripcion = models.TextField()

    def generarFactura(self):
        pass

class Transaccion(models.Model):
    idTransaccion = models.CharField(max_length=10, unique=True)
    fechaTransaccion = models.DateField()
    monto = models.FloatField()

    def procesarTransaccion(self):
        pass

class Pago(models.Model):
    class Meta:
        abstract = True

    def procesarPago(self):
        pass

class PagoTarjeta(Pago):
    numeroTarjeta = models.CharField(max_length=16)
    nombreDueño = models.CharField(max_length=50)
    fechaExpiracion = models.DateField()

    def realizarPago(self):
        pass

class PagoEfectivo(Pago):
    def realizarPago(self):
    pass

class CheckIn(models.Model):
    fecha = models.DateField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    habitacion = models.ForeignKey(Habitacion, on_delete=models.CASCADE)

    def realizarCheckIn(self):
        pass

class CheckOut(models.Model):
    fecha = models.DateField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    habitacion = models.ForeignKey(Habitacion, on_delete=models.CASCADE)

    def realizarCheckOut(self):
        pass

