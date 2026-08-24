from ClasesDatos.JsonPropiedad import JsonPropiedad
from ClasesNegocios.Validadores import ValidadorPropiedades
from ClasesNegocios.Validadores import ValidadorReservas

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
      return "Tipo de propiedad: {}, Ubicacion de la casa: {}, Cantidad maxima de personas: {}, Precio por noche: {}, Identificacion: {}, numero del dueño: {}".format(self.__tipo_propie, self.__ubicacion, self.__maxima_personas, self.__precio_noche, self.__identificacion_dueno, self.__contacto)


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


    def buscar_precio(self):
        propiedad = JsonPropiedad()
        return propiedad.buscar_precio(self.ID_Sitio)


    @classmethod
    def leer_propiedades(cls):
        propiedad = JsonPropiedad()
        return propiedad.leer_propiedades()

    
    def registrar_propiedad(self): 
        propiedad= JsonPropiedad()
        ValidadorReservas.ValidadorReservas.validar_identificacion(int(self.Identificacion))
        ValidadorPropiedades.ValidadorPropiedades.validar_propiedad(self.Tipo_propie, self.Ubicacion, self.Maxima_personas, self.Precio_noche, self.Contacto)


        propiedad.registrar_propiedad(self.Identificacion, self.ID_Sitio, self.Tipo_propie, self.Ubicacion,
                                      self.Maxima_personas, self.Precio_noche, self.contacto)


    @classmethod
    def editar_propiedad(cls, id_sitio, tipo_propie, ubicacion, maxima_personas, precio_noche, contacto):
        propiedad= JsonPropiedad()
        return propiedad.editar_propiedad(id_sitio, tipo_propie, ubicacion,
                                   maxima_personas, precio_noche, contacto)



    def eliminar_propiedad(self):

        propiedad = JsonPropiedad()
        propiedad.eliminar_propiedad(self.ID_Sitio)

