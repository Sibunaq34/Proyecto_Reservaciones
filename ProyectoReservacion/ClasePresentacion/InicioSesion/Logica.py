from tkinter import messagebox
from ClasesNegocios.Usuarios import Usuarios
from ClasePresentacion.InicioSesion.DisenoIniciarSesion import FormularioInicioSesion
from ClasePresentacion.InicioSesion.DisenoRegistrar import FormularioRegistrar
from ClasePresentacion.Principal.Index.PaginaPrincipal import PaginaPrincipal

class InicioSesion(FormularioInicioSesion):
    
    def registro(self):
        FormularioRegistrar()

    def validacion(self):
        usuarios = Usuarios()
        email = self.usuario.get()
        password = self.contrasena.get()



        if usuarios.iniciar_sesion("Cliente",email, password):
            identificacion = usuarios.buscar_usuario("Cliente", email)
            self.ventana.destroy()
            PaginaPrincipal("Cliente", identificacion)## Envia la contrasena e email que se ingresaron a la hora de iniciar sesion
            return
        elif usuarios.iniciar_sesion("Dueno",email, password):
            identificacion = usuarios.buscar_usuario("Dueno", email)
            self.ventana.destroy()
            PaginaPrincipal("Dueno", identificacion)
            return
        else:
            self.ventana.destroy()
            PaginaPrincipal("Admin", email)

        messagebox.showerror(message="La contraseña es incorrecta", title="Mensaje")

    def __init__(self):
        super().__init__()
