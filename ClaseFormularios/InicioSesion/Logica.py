import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.font import BOLD
from ClasesDatos.Dueno import ArchivoDuenos
from ClasesDatos.Clientes import ArchivoClientes
from ClasesDatos.UsuarioAdmin import UsuarioAdmin
from ClaseFormularios.InicioSesion.DisenoIniciarSesion import FormularioInicioSesion
from ClaseFormularios.InicioSesion.DisenoRegistrar import FormularioRegistrar
from ClaseFormularios.Principal.Admin.PaginaPrincipalAdmin import PaginaPrincipal
from ClaseFormularios.Principal.Clientes.PaginaPrincipalC import PaginaPrincipalC
from ClaseFormularios.Principal.Duenos.PaginaPrincipalDuenos import PaginaPrincipalDuenos

class InicioSesion(FormularioInicioSesion):
    
    def registro(self):
        FormularioRegistrar()

    def validacion(self):
        admin = UsuarioAdmin()
        cliente = ArchivoClientes()
        duenos = ArchivoDuenos()
        email = self.usuario.get()
        password = self.contrasena.get()

        usuario = admin.buscar_usuario(email,password) 

        if usuario:
            self.ventana.destroy()
            PaginaPrincipal()
            return

        usuario = cliente.inicioSesion(email, password) 

        if usuario:
            self.ventana.destroy()
            PaginaPrincipalC(email, password) ## Envia la contrasena e email que se ingresaron a la hora de iniciar sesion
            return

        usuario = duenos.inicioSesion(email, password)
        if usuario:
            self.ventana.destroy()
            PaginaPrincipalDuenos(email, password)
            return

        messagebox.showerror(message="La contraseña es incorrecta", title="Mensaje")

    def __init__(self):
        super().__init__()
