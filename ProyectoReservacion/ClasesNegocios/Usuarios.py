class Usuarios:
 # Metodo constructor
    def __init__(self, identificacion, nombre, apellido, email, contrasena, tipo):
        self.__identificacion = identificacion
        self.__nombre = nombre
        self.__apellido = apellido
        self.__email = email
        self.__contrasena = contrasena
        self.__tipo = tipo

        if not isinstance(identificacion, int):
            raise ValueError("Se debe de ingresar un numero")    
        elif identificacion <=0:
            raise ValueError("El numero de identificacion no puede ser negativo") 
        if identificacion == "":
           raise ValueError("Se debe de ingresar la identificacion")
        
        if nombre == "":
         raise ValueError("Se debe de ingresar un nombre")
        
        if apellido =="":
            raise ValueError("Se debe de ingresar el apellido")
        if email =="":
            raise ValueError("Se debe de ingresar el correo electronico(Email)")
        
        if contrasena =="":
            raise ValueError("Se debe de ingresar una contraseña")
        
        if tipo != "Dueno" and tipo != "Cliente":
            raise ValueError("La opcion es incorrecta")

    

# Metodo string para mostrar datos
    def __str__(self):
      return "Identificacion: {}, Nombre: {}, Apellido: {}, Email: {}, Tipo de usuario{}".format(self.__identificacion, self.__nombre, self.__apellido, self.__email, self.__tipo)
  

    @property
    def Identificacion(self):
        return self.__identificacion
    @Identificacion.setter
    def Identificacion(self, valor):
        self.__identificacion = valor


    @property
    def Nombre(self):
        return self.__nombre
    @Nombre.setter
    def Nombre(self, valor):
        self.__nombre = valor

    
    @property
    def Apellido(self):
        return self.__apellido
    @Apellido.setter
    def Apellido(self, valor):
        self.__apellido = valor


    @property
    def Email(self):
        return self.__email 
    @Email.setter
    def Email(self, valor):
        self.__email = valor

    @property
    def Contrasena(self): 
       return self.__contrasena
    @Contrasena.setter
    def Contrasena(self, valor):
       self.__contrasena = valor
    
    
    @property 
    def Tipo(self):
       return self.__tipo
    @Tipo.setter
    def Tipo(self, valor):
        self.__tipo = valor