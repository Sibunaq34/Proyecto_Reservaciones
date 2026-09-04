from datetime import datetime

class ValidadorReservas:


    @staticmethod
    def validar_formato_fechas(fecha):

        try:
            fecha = datetime.strptime(fecha, "%d/%m/%Y")
            return fecha
        except ValueError:
            raise ValueError("Formato de fecha inválido. Use el formato DD/MM/AAAA.")


    @staticmethod
    def validar_fechas(fecha_entrada, fecha_salida):
        fecha_entrada = datetime.strptime(fecha_entrada, "%d/%m/%Y")
        fecha_salida = datetime.strptime(fecha_salida, "%d/%m/%Y")
        if fecha_entrada >= fecha_salida:
            raise ValueError("La fecha de salida debe ser posterior a la de entrada.")


    @staticmethod
    def validar_cantidad_personas(cantidad_personas):

        if not isinstance(cantidad_personas, int):
            raise ValueError("La cantidad de personas debe de ser un numero entero")    
        elif cantidad_personas <=0:
            raise ValueError("La cantidad de personas no puede ser negativa") 
        if cantidad_personas == "":
           raise ValueError("Se debe de ingresar la cantidad de personas")


    @staticmethod
    def validar_identificacion(identificacion):
        if not isinstance(identificacion, int):
            raise ValueError("La identificacion debe de ser solo numeros")    
        elif identificacion <=0:
            raise ValueError("El numero de identificacion no puede ser negativo") 
        if identificacion == "":
           raise ValueError("Se debe de ingresar la identificacion")

        if not str(identificacion).startswith(('1', '2', '3', '4', '5', '6', '7', '8')):
            raise ValueError("La identificacion debe de empezar con 1, 2, 3, 4, 5, 6, 7 o 8")

        if len(str(identificacion)) != 9:
            raise ValueError("La identificacion debe de tener 9 digitos")