from ClasesDatos.JsonPropiedad import JsonPropiedad
from ClasesNegocios.Validadores.ValidadorPropiedades import ValidadorPropiedades
from ClasesNegocios.Validadores.ValidadorReservas import ValidadorReservas

class Propiedades:
    # Metodo constructor
    def __init__(self):
        self.json_propiedad = JsonPropiedad()
        

# Metodo string para mostrar datos

    def buscar_precio(self, id_sitio):
        id_sitio = int(id_sitio)
        propiedad = self.json_propiedad.buscar_precio(id_sitio)
        return propiedad


    def leer_propiedades(self):
        propiedad = self.json_propiedad.leer_propiedades()
        return propiedad["propiedades"]["usuario"]

    
    def registrar_propiedad(self, identificacion, id_sitio, tipo_propie, ubicacion, maxima_personas, precio_noche, contacto):

        ValidadorReservas.validar_identificacion(int(identificacion))
        ValidadorPropiedades.validar_propiedad(tipo_propie, ubicacion, maxima_personas, precio_noche, contacto)

        self.json_propiedad.registrar_propiedad(identificacion, id_sitio, tipo_propie, ubicacion,
                                      maxima_personas, precio_noche, contacto)


    def editar_propiedad(self, id_sitio, tipo_propie, ubicacion, maxima_personas, precio_noche, contacto):

        return self.json_propiedad.editar_propiedad(id_sitio, tipo_propie, ubicacion,
                                   maxima_personas, precio_noche, contacto)


    def eliminar_propiedad(self, id_sitio):
        id_sitio = int(id_sitio)
        propiedad = self.json_propiedad.eliminar_propiedad(id_sitio)
        return propiedad

