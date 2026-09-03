class ValidadorPropiedades:

       @staticmethod
       def validar_propiedad(tipo_propie, ubicacion, maxima_personas, precio_noche, contacto):

            if tipo_propie == "":
                raise ValueError("Debe de ingresar el tipo de propiedad")
        
            if  ubicacion == "":
                raise ValueError("Debe de ingresar la ubicacion de la propiedad")

        
            if not isinstance(maxima_personas, int):
                raise ValueError("Se debe de ingresar un numero")   
            if maxima_personas < 1:
                raise ValueError("La cantidad maxima de personas debe ser mayor a 1")
            if maxima_personas > 30:
                raise ValueError("La cantidad maxima de personas debe de ser menor a 30")
            if maxima_personas == "":
                raise ValueError("La cantidad maxima de personas no puede estar vacio")

            
            if not isinstance(precio_noche, int):
                raise ValueError("Se debe de ingresar un numero")
            if precio_noche < 5000:
                raise ValueError("El precio minimo es 5000")
            if precio_noche == "":
                raise ValueError("Se debe de ingresar el precio")

            
            if contacto == "":
                raise ValueError("Ingrese el numero de telefono")
            if len(str(contacto)) != 8:
                raise ValueError("El numero de contacto debe de tener 8 digitos")