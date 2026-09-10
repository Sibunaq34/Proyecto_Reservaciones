import os
import json

class JsonPropiedad:


    def __init__(self, archivo="ClasesDatos/Archivos/propiedades.json"):
        self.archivo = archivo
        if not os.path.exists(self.archivo):
            estructura = {
                "propiedades":{
                    "usuario":[]
                }
            }
            with open(self.archivo, "w", encoding="utf-8") as f:
                json.dump(estructura, f, indent=4)



    def registrar_propiedad (self, identificacion, id_sitio, tipo_propie, ubicacion, maxima_personas,
                             precio_noche, contacto):

        datos = self.leer_propiedades()
        lista_propiedades = datos["propiedades"]["usuario"]

        propiedad = {
            "Identificacion": str(identificacion),
            "ID del sitio": int(id_sitio),
            "Tipo de Propiedad": tipo_propie,
            "Ubicacion": ubicacion,
            "Cantidad maxima de personas": maxima_personas,
            "Precio por noche": precio_noche,
            "Contacto": contacto

        }

        lista_propiedades.append(propiedad)

        with open(self.archivo, "w", encoding="utf-8") as f:
            json.dump(datos, f, indent=4)

        return propiedad


    def leer_propiedades(self):

        with open(self.archivo, "r", encoding="utf-8") as f: return json.load(f)

    
    def editar_propiedad(self, id_sitio, tipo_propie, ubicacion, maxima_personas, precio_noche, contacto):

        datos = self.leer_propiedades()
        lista_propiedades = datos["propiedades"]["usuario"]

        for propiedad in lista_propiedades:
            if propiedad["ID del sitio"] == int(id_sitio):
                propiedad["ID del sitio"] = int(id_sitio)
                propiedad["Tipo de Propiedad"] = tipo_propie
                propiedad["Ubicacion"] = ubicacion
                propiedad["Cantidad maxima de personas"] = maxima_personas
                propiedad["Precio por noche"] = precio_noche
                propiedad["Contacto"] = contacto

            with open(self.archivo, "w", encoding="utf-8") as f:
                json.dump(datos, f, indent=4)
        return propiedad

    
    def eliminar_propiedad(self, id_sitio):

        datos = self.leer_propiedades()
        lista_propiedades = datos ["propiedades"]["usuario"]

        for i, reservacion in enumerate(lista_propiedades):
            if reservacion["ID del sitio"] == int(id_sitio):
                    lista_propiedades.pop(i)
                    with open(self.archivo, "w", encoding="utf-8") as f:
                        json.dump(datos, f, indent=4)
                    return reservacion

              
    def buscar_precio(self, id_sitio):

        datos = self.leer_propiedades()
        lista_propiedades = datos ["propiedades"]["usuario"]

        for propiedades in lista_propiedades:
            if propiedades["ID del sitio"] == int(id_sitio):
                return propiedades["Precio por noche"]

        return 0