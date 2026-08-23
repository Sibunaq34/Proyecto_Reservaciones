import os
import json

class JsonReservaciones:


    def __init__(self, archivo="Datos/Archivos/reservaciones.json"):
        self.archivo = archivo
        if not os.path.exists(self.archivo):
            estructura = {
                "Reservaciones":{
                    "Clientes":[]
                }
            }
            with open(self.archivo, "w", encoding="utf-8") as f:
                json.dump(estructura, f, indent=4)


    def registrar_reservacion (self, identificacion, id_sitio, fecha_entrada, fecha_salida, disponible, cantidad_personas, total):

        datos = self.leer_reserva()

        lista_reservaciones = datos["Reservaciones"]["Clientes"]

        nueva_reservacion = {
            "Identificacion": str(identificacion),  
            "ID Sitio": id_sitio,
            "Fecha de entrada": fecha_entrada,
            "Fecha de salida": fecha_salida,
            "Disponibilidad": disponible,
            "Cantidad de personas": cantidad_personas,
            "Total": total
        }

        lista_reservaciones.append(nueva_reservacion)

        with open(self.archivo, "w", encoding="utf-8") as f:
            json.dump(datos, f, indent=4)

        return nueva_reservacion

    
    def leer_reserva(self):
        with open(self.archivo, "r", encoding="utf-8") as f: return json.load(f)


    def editar_reserva(self, identificacion, id_sitio, fecha_entrada, 
                       fecha_salida, disponible, cantidad_personas, total):

        datos = self.leer_reserva()
        lista_reservaciones = datos["Reservaciones"]["Clientes"]

        for reservacion in lista_reservaciones:
            if reservacion["Identificacion"] == str(identificacion) and reservacion["ID Sitio"] == id_sitio and reservacion["Fecha de entrada"] == fecha_entrada and reservacion["Fecha de salida"] == fecha_salida:
                reservacion["Fecha de entrada"] = fecha_entrada
                reservacion["Fecha de salida"] = fecha_salida
                reservacion["Disponibilidad"] = disponible
                reservacion["Cantidad de personas"] = cantidad_personas
                reservacion["Total"] = total

                with open(self.archivo, "w", encoding="utf-8") as f:
                    json.dump(datos, f, indent=4)
                return reservacion

        raise ValueError("No se encontró la reservación con los criterios especificados.")

    
    def eliminar_reserva(self, identificacion , id_sitio, fecha_entrada, fecha_salida):

        datos = self.leer_reserva()
        lista_reservaciones = datos["Reservaciones"]["Clientes"]

        for i, reservacion in enumerate(lista_reservaciones):
            if reservacion["Identificacion"] == str(identificacion) and reservacion["ID Sitio"] == id_sitio and reservacion["Fecha de entrada"] == fecha_entrada and reservacion["Fecha de salida"] == fecha_salida:
                lista_reservaciones.pop(i)
                with open(self.archivo, "w", encoding="utf-8") as f:
                    json.dump(datos, f, indent=4)
                return reservacion

        raise ValueError("No se encontró la reservación con los criterios especificados.")


    def validacion_fecha(self, id_sitio, fecha_entrada, fecha_salida,
                         identificacion=None):
        datos = self.leer_reserva()
        lista_reservaciones = datos["Reservaciones"]["Clientes"]

        for reservacion in lista_reservaciones:
            es_reserva_actual = (
                identificacion is not None and
                reservacion["Identificacion"] == str(identificacion) and
                str(reservacion["ID Sitio"]) == str(id_sitio) and
                reservacion["Fecha de entrada"] == fecha_entrada and
                reservacion["Fecha de salida"] == fecha_salida
            )
            if es_reserva_actual:
                continue
            if (str(reservacion["ID Sitio"]) == str(id_sitio) and
                fecha_entrada <= reservacion["Fecha de salida"] and
                fecha_salida >= reservacion["Fecha de entrada"]):
                return True

        return False   

    
    def buscar_reserva(self, identificacion, id_sitio, fecha_entrada, fecha_salida):

        leer_reservaciones = self.leer_reserva()
        lista_reservaciones = leer_reservaciones["Reservaciones"]["Clientes"]

        for reservacion in lista_reservaciones:
            if (reservacion["Identificacion"] == str(identificacion) and
                reservacion["ID Sitio"] == id_sitio and
                reservacion["Fecha de entrada"] == fecha_entrada and
                reservacion["Fecha de salida"] == fecha_salida):
                return reservacion["Total"]
        return None

