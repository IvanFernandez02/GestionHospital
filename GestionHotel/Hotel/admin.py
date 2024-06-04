from django.contrib import admin

from Hotel.models import *

# Register your models here.
admin.site.register(Persona)
admin.site.register(Cliente)
admin.site.register(Empleado)
admin.site.register(TipoHabitacion)
admin.site.register(Habitacion)
admin.site.register(EstadoReserva)
admin.site.register(Reservacion)
admin.site.register(Factura)
admin.site.register(Transaccion)
admin.site.register(Pago)
admin.site.register(PagoTarjeta)
admin.site.register(PagoEfectivo)
admin.site.register(CheckIn)
admin.site.register(CheckOut)



