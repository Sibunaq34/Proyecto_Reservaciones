from ClasesDatos.JsonPropiedad import JsonPropiedad
from ClasesNegocios.Validadores.ValidadorPropiedades import ValidadorPropiedades
from ClasesNegocios.Validadores.ValidadorReservas import ValidadorReservas

class Propiedades:
    # Metodo constructor
    def __init__(self,identificacion, id_sitio, tipo_propie, ubicacion, maxima_personas, precio_noche,contacto):
        self.__identificacion= identificacion
        self.__id_sitio = id_sitio
        self.__tipo_propie = tipo_propie
        self.__ubicacion = ubicacion
        self.__maxima_personas = maxima_personas
        self.__precio_noche = precio_noche
        self.__contacto = contacto
        

# Metodo string para mostrar datos
    def __str__(self):
      return "Identificacion{}, ID del Sitio{} Tipo de propiedad: {}, Ubicacion de la casa: {}, Cantidad maxima de personas: {}, Precio por noche: {}, Identificacion: {}, numero del dueño: {}".format(self.__identificacion, self.__id_sitio, self.__tipo_propie, self.__ubicacion, self.__maxima_personas, self.__precio_noche, self.__contacto)


    @property
    def Identificacion(self):
        return self.__identificacion
    @Identificacion.setter
    def Identificacion(self, valor):
        self.__identificacion = valor


    @property
    def ID_Sitio(self):
        return self.__id_sitio
    @ID_Sitio.setter
    def ID_Sitio(self, valor):
        self.__id_sitio = valor


    @property
    def Tipo_propie(self):
        return self.__tipo_propie
    @Tipo_propie.setter
    def Tipo_propie(self, valor):
        self.__tipo_propie = valor


    @property
    def Ubicacion(self):
        return self.__ubicacion
    @Ubicacion.setter
    def Ubicacion(self, valor):
        self.__ubicacion = valor


    @property
    def Maxima_personas(self):
        return self.__maxima_personas
    @Maxima_personas.setter
    def Maxima_personas(self, valor):
        self.__maxima_personas = valor


    @property
    def Precio_noche(self):
        return self.__precio_noche
    @Precio_noche.setter
    def Precio_noche(self, valor):
        self.__precio_noche = valor


    @property
    def Contacto(self):
        return self.__contacto
    @Contacto.setter
    def contacto(self, valor):
        self.__contacto = valor


    @staticmethod
    def buscar_precio(id_sitio):
        propiedad = JsonPropiedad()
        precio = propiedad.buscar_precio(id_sitio)
        return precio

    @classmethod
    def leer_propiedades(cls):
        propiedad = JsonPropiedad()
        return propiedad.leer_propiedades()

    
    def registrar_propiedad(self): 
        propiedad= JsonPropiedad()
        ValidadorReservas.validar_identificacion(int(self.Identificacion))
        ValidadorPropiedades.validar_propiedad(self.Tipo_propie, self.Ubicacion, self.Maxima_personas, self.Precio_noche, self.Contacto)


        propiedad.registrar_propiedad(self.Identificacion, self.ID_Sitio, self.Tipo_propie, self.Ubicacion,
                                      self.Maxima_personas, self.Precio_noche, self.contacto)


    @classmethod
    def editar_propiedad(cls, id_sitio, tipo_propie, ubicacion, maxima_personas, precio_noche, contacto):
        propiedad= JsonPropiedad()
        return propiedad.editar_propiedad(int(id_sitio), tipo_propie, ubicacion,
                                   maxima_personas, precio_noche, contacto)


    @classmethod
    def eliminar_propiedad(cls, id_sitio):

        propiedad = JsonPropiedad()
        propiedad.eliminar_propiedad(int(id_sitio))
        return True

