from ClasesDatos.Usuarios import ArchivosUsuarios

class ValidarUsuario:


    def __init__(self):
        self.archivo = ArchivosUsuarios()


    @staticmethod
    def validar_identificacion(identificacion):
        if not isinstance(identificacion, int):
            raise ValueError("La identificacion debe de ser solo numeros")
        elif identificacion <= 0:
            raise ValueError("El numero de identificacion no puede ser negativo")
        if identificacion == "":
            raise ValueError("Se debe de ingresar la identificacion")

        if not str(identificacion).startswith(('1', '2', '3', '4', '5', '6', '7', '8')):
            raise ValueError("La identificacion debe de empezar con 1, 2, 3, 4, 5, 6, 7 o 8")

        if len(str(identificacion)) != 9:
            raise ValueError("La identificacion debe de tener 9 digitos")


    @staticmethod
    def nombre_usuario(nombre, apellido):
        if nombre == "":
            raise ValueError("Se debe de ingresar un nombre")

        if apellido == "":
            raise ValueError("Se debe de ingresar el apellido")

        if any(char.isdigit() for char in nombre):
            raise ValueError("El nombre no debe contener numeros")
        if any(char.isdigit() for char in apellido):
            raise ValueError("El apellido no debe contener numeros")


    @staticmethod
    def email_usuario(email):

        if email == "":
            raise ValueError("Se debe de ingresar el correo electronico(Email)")


        if "@" not in email:
            raise ValueError("El correo ingresado no es valido")


    @staticmethod
    def contrasena_usuario(contrasena):

        if contrasena == "":
            raise ValueError("Se debe de ingresar una contraseña")

        if len(str(contrasena)) <8:
            raise ValueError("La contrasena debe de tener al menos 8 caracteres")
        elif len(str(contrasena)) > 16:
            raise ValueError("La contrasena no debe sobre pasar los 16 caracteres")


    def validar_registro(self, tipo, identificacion, email):

        if self.archivo.validar_regisrtro(tipo, identificacion, email):
            raise ValueError("El correo o la Identificacion ya fueron registrados anteriormente")
