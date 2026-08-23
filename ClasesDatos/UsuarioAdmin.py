import os

class UsuarioAdmin:

    def __init__(self):
        self.ruta_archivo = os.path.join(os.path.dirname(__file__), '../ClasesDatos/Datos/Usuarios.txt')

    def buscar_usuario(self, email, contrasena):
        try:
            with open(self.ruta_archivo, 'r', encoding='utf-8') as archivo:
                for linea in archivo:
                    if "Email:" in linea and "Contrasena:" in linea:
                        datos = self.parsear_linea(linea)
                        if datos.get("Email") == email and datos.get("Contrasena") == contrasena:
                            return datos
            return None  # No se encontró usuario
        except Exception as e:
            print(f"Error leyendo archivo de usuarios: {e}")
            return None

    def parsear_linea(self, linea):
        partes = linea.strip().split(", ")
        datos = {}
        for parte in partes:
            if ": " in parte:
                clave, valor = parte.split(": ", 1)
                datos[clave.strip()] = valor.strip()
        return datos