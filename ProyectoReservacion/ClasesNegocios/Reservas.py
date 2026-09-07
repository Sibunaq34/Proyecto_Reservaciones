from ClasesDatos.JsonReservaciones import JsonReservaciones
from ClasesNegocios.Validadores.ValidadorReservas import ValidadorReservas

class Reservas:


    def __init__(self):
        self.json_reservaciones = JsonReservaciones()


    def registrar_reserva(self, identificacion, id_sitio, fecha_entrada, fecha_salida,
                          disponible, cantidad_personas, total):
        reserva = JsonReservaciones()

        fecha1 = ValidadorReservas.validar_formato_fechas(fecha_entrada)
        fecha2= ValidadorReservas.validar_formato_fechas(fecha_salida)
        ValidadorReservas.validar_fechas(fecha_entrada, fecha_salida)
        ValidadorReservas.validar_cantidad_personas(cantidad_personas)
        ValidadorReservas.validar_identificacion(identificacion)

        dias = (fecha2 - fecha1).days
        dias = abs(dias)
        total = dias * total

        validacion = self.json_reservaciones.validacion_fecha(id_sitio, fecha_entrada, fecha_salida)
        if not validacion:
            reserva.registrar_reservacion(str(identificacion), int(id_sitio), fecha_entrada,
                                     fecha_salida, disponible, int(cantidad_personas), int(total))
        else :
            raise ValueError("Ya existe una reservacion en esas fechas, por favor elija otras fechas para su reservacion")


    def eliminar_reserva(self, identificacion):
        return self.json_reservaciones.eliminar_reserva(identificacion)


    def leer_reserva(self):
        reserva = self.json_reservaciones.leer_reserva()
        return reserva["Reservaciones"]["Usuario"]


    def editar_reserva(self, id_reservacion, identificacion, id_sitio, fecha_entrada, fecha_salida, disponible, cantidad_personas, total):

        fecha1= ValidadorReservas.validar_formato_fechas(fecha_entrada)
        fecha2=ValidadorReservas.validar_formato_fechas(fecha_salida)
        ValidadorReservas.validar_fechas(fecha_entrada, fecha_salida)
        ValidadorReservas.validar_cantidad_personas(int(cantidad_personas))

        dias = (fecha2 - fecha1).days
        dias = abs(dias)
        total = dias * total
        validacion = self.json_reservaciones.validacion_fecha(id_sitio, identificacion, fecha_entrada, fecha_salida)
        if not validacion:
            self.json_reservaciones.editar_reserva(int(id_reservacion), fecha_entrada,
                                fecha_salida, disponible, int(cantidad_personas), int(total))
        else:
            raise ValueError("Ya existe una reservacion en esas fechas, por favor elija otras fechas para su reservacion")


    def buscar_reserva(self, identificacion, id_sitio, fecha_entrada, fecha_salida):
        return self.json_reservaciones.buscar_reserva(identificacion, id_sitio, fecha_entrada, fecha_salida)


    def validacion_fecha(self, id_sitio, fecha_entrada, fecha_salida):
        return self.json_reservaciones.validacion_fecha(id_sitio, fecha_entrada,fecha_salida)

