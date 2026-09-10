from ClasesNegocios.Validadores.ValidarUsuarios import ValidarUsuario
from ClasesDatos.Usuarios import ArchivosUsuarios
from ClasesDatos.UsuarioAdmin import UsuarioAdmin

class Usuarios:
 # Metodo constructor
    def __init__(self):
        self.xml_clientes = ArchivosUsuarios()
        self.text_admin = UsuarioAdmin()


    def registrar_usuario(self, tipo, identificacion, nombre, apellido, email, contrasena):
        ValidarUsuario.validar_identificacion(identificacion)
        ValidarUsuario.nombre_usuario(nombre, apellido)
        ValidarUsuario.email_usuario(email)
        ValidarUsuario.contrasena_usuario(contrasena)
        usuario= ValidarUsuario()
        usuario.validar_registro(tipo, identificacion, email)
        return self.xml_clientes.escribir_xml(tipo, identificacion, nombre, apellido, email, contrasena)


    def leer_usuarios(self):
        return  self.xml_clientes.leer_xml()


    def leer_cliente(self):
        return self.xml_clientes.leer_clientes()


    def leer_duenos(self):
        return self.xml_clientes.leer_duenos()


    def filtrar_usuarios(self, tipo, identificacion):
        return self.xml_clientes.filtrar_usuarios(tipo, identificacion)


    def editar_usuario(self, tipo, identificacion, nombre, apellido, email, contrasena):
        ValidarUsuario.validar_identificacion(identificacion)
        ValidarUsuario.nombre_usuario(nombre, apellido)
        ValidarUsuario.email_usuario(email)
        ValidarUsuario.contrasena_usuario(contrasena)
        return self.xml_clientes.modificar_xml(tipo, identificacion, nombre, apellido, email, contrasena)


    def eliminar_usuario(self, tipo, identificacion):
        return self.xml_clientes.eliminar_usuario(tipo, identificacion)


    def iniciar_sesion(self,tipo, email, contrasena):
        if tipo == "Admin":
            return self.text_admin.buscar_usuario(email, contrasena)
        else:
            return self.xml_clientes.inicio_sesion(tipo, email, contrasena)


    def buscar_usuario(self, tipo, email):
        return self.xml_clientes.buscar_usuario(tipo, email)


    def validar_usuario(self, tipo, identificacion):
        return self.xml_clientes.validar_usuario(tipo, str(identificacion))