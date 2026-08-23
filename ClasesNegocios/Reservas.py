from ClasesDatos.JsonReservaciones import *
from Validadores.ValidadorReservas import *
import datetime
class Reservas:
    def __init__(self, identificacion, id_sitio, fecha_entrada, fecha_salida, disponible, cantidad_personas, total):
        self.__identificacion = identificacion
        self.__id_sitio = id_sitio
        self.__fecha_entrada = fecha_entrada
        self.__fecha_salida = fecha_salida
        self.__disponible = disponible
        self.__cantidad_personas= cantidad_personas
        self.__total = total

    def __str__(self):
        return "Identificacion: {}\nID Sitio: {}\nFecha Entrada: {}\nFecha Salida: {}\nDisponible: {}\nCanditidad de personas a ir: {}\nCosto total a pagar: {}".format(self.__identificacion, self.__id_sitio, self.__fecha_entrada, self.__fecha_salida, self.__disponible, self.__cantidad_personas, self.__total)
    

    @property
    def Identificacion(self):
        return self.__identificacion
    @Identificacion.setter
    def Identificacion(self, valor):
        self.__identificacion = valor

        
    @property
    def Id_sitio(self):
        return self.__id_sitio
    @Id_sitio.setter
    def Id_sitio(self, valor):
        self.__id_sitio = valor
    

    @property
    def Fecha_entrada(self):
        return self.__fecha_entrada
    @Fecha_entrada.setter
    def Fecha_entrada(self, valor):
        self.__fecha_entrada = valor
    

    @property
    def Fecha_salida(self):
        return self.__fecha_salida
    @Fecha_salida.setter
    def Fecha_salida(self, valor):
        self.__fecha_salida = valor


    @property
    def Disponible(self): 
        return self.__disponible
    @Disponible.setter
    def Disponible(self, valor):
        self.__disponible = valor
    

    @property
    def Cantidad_Personas(self):
        return self.__cantidad_personas
    @Cantidad_Personas.setter
    def Cantidad_Personas(self, valor):
        self.__cantidad_personas = valor


    @property
    def Total(self):
        return self.__total
    @Total.setter
    def Total(self, valor):
        self.__total = valor


    def registrar_reserva(self):
        reserva = JsonReservaciones()

        fecha1 = ValidadorReservas.validar_formato_fechas(self.Fecha_entrada)
        fecha2= ValidadorReservas.validar_formato_fechas(self.Fecha_salida)
        ValidadorReservas.validar_fechas(self.Fecha_entrada, self.Fecha_salida)
        ValidadorReservas.validar_cantidad_personas(self.Cantidad_Personas)
        ValidadorReservas.validar_identificacion(self.Identificacion)

        dias = (fecha2 - fecha1).days
        dias = abs(dias)
        self.Total = dias * self.Total

        validacion = reserva.validacion_fecha(self.Id_sitio, self.Fecha_entrada, self.Fecha_salida)
        if  validacion == False:
            reserva.registrar_reservacion(self.Identificacion, self.Id_sitio, self.Fecha_entrada, 
                                     self.Fecha_salida, self.Disponible, self.Cantidad_Personas, self.Total)
        else :
            raise ValueError("Ya existe una reservacion en esas fechas, por favor elija otras fechas para su reservacion")


    def eliminar_reserva(self):
        ValidadorReservas.validar_formato_fechas(self.Fecha_entrada, self.Fecha_salida)
        reserva = JsonReservaciones()
        return reserva.eliminar_reserva(self.Identificacion,self.Id_sitio, self.Fecha_entrada, self.Fecha_salida)

    def leer_reserva(self):
        reserva = JsonReservaciones()
        return reserva.leer_reserva()


    def editar_reserva(self):
        reserva = JsonReservaciones()
        
        fecha1= ValidadorReservas.validar_formato_fechas(self.Fecha_entrada)
        fecha2=ValidadorReservas.validar_formato_fechas(self.Fecha_salida)
        ValidadorReservas.validar_fechas(self.Fecha_entrada, self.Fecha_salida)
        ValidadorReservas.validar_cantidad_personas(self.Cantidad_Personas)

        dias = (fecha2 - fecha1).days
        dias = abs(dias)
        self.Total = dias * self.Total
        validacion = reserva.validacion_fecha(self.Id_sitio, self.Identificacion, self.Fecha_entrada, self.Fecha_salida)
        if validacion == False:
            reserva.editar_reserva(self.Identificacion, self.Id_sitio, self.Fecha_entrada, 
                                self.Fecha_salida, self.Disponible, self.Cantidad_Personas, self.Total)
        else:
            raise ValueError("Ya existe una reservacion en esas fechas, por favor elija otras fechas para su reservacion")


    def buscar_reserva(self):
        reserva = JsonReservaciones()
        return reserva.buscar_reserva(self.Identificacion, self.Id_sitio, self.Fecha_entrada, self.Fecha_salida)


    def validacion_fecha(self):
        reserva = JsonReservaciones()
        return reserva.validacion_fecha(self.Id_sitio, self.Fecha_entrada, self.Fecha_salida)

