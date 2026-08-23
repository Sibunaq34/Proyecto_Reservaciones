import tkinter as tk
from tkinter.font import BOLD
from ClaseFormularios.Principal.Clientes.CRUDClientes.EditarCliente import *
from ClaseFormularios.Principal.Clientes.CRUDClientes.EliminarCliente import *

from ClaseFormularios.Principal.Clientes.CRUDReservaciones.EditarRerservacion import *
from ClaseFormularios.Principal.Clientes.CRUDReservaciones.EliminarReservacion import *
from ClaseFormularios.Principal.Clientes.CRUDReservaciones.RegistrarReservacion import *

class PaginaPrincipalC: 
    
    def __init__(self, email, contrasena): #Recibe los datos para del inicio de sesion 
        self.email = email
        self.contrasena= contrasena
        self.ventana = tk.Tk()
        self.ventana.title("Paginal Principal")
        w, h = self.ventana.winfo_screenwidth(), self.ventana.winfo_screenheight()
        self.ventana.geometry("%dx%d+0+0" % (w, h))
        self.ventana.config(bg="#238799")
        self.ventana.resizable(True, True)
        self.ventana.state("zoomed")

        label = tk.Label(self.ventana)
        label.place(x=0, y=0, relwidth=1, relheight=1)
        
        MSmenu= tk.Menu(self.ventana)
        self.ventana.config(menu=MSmenu)

        #Region Menu Strip

        menu_cliente = tk.Menu(MSmenu, tearoff=0) #Crea la bandeja del menu
        menu_reservas = tk.Menu(MSmenu, tearoff=0)
        MSmenu.add_cascade(label="Clientes", menu=menu_cliente)
        MSmenu.add_cascade(label="Reservaciones", menu=menu_reservas)   #Agrega las opciones principales esto con el add cascade
        MSmenu.add_cascade(label="Acerca de", command=self.acerca_de)
        MSmenu.add_cascade(label="Salir", command=self.ventana.destroy)

        #Submenu cliente
        #Agrega las opciones que estaran en el boton de Clientes generado por MSmenu, mas genera la accion para el boton
        menu_cliente.add_command(label="Editar Cuenta", command=self.ventanaEditarCliente)
        menu_cliente.add_command(label="Eliminar Cuenta", command=self.ventanaEliminarCliente)

        #sub menu reservacion
        menu_reservas.add_command(label="Registrar", command=self.ventanaEditarReserva) #Agrega las opciones que estaran en el boton de Clientes generado por MSmenu, mas genera la accion para el boton
        menu_reservas.add_command(label="Editar", command=self.ventanaEditarReserva)
        menu_reservas.add_command(label="Eliminar", command=self.ventanaEliminarReserva)
        self.ventana.mainloop()
    
    def acerca_de(self):
        ventana_acerca = tk.Toplevel(self.ventana)
        ventana_acerca.title("Acerca de")
        ventana_acerca.geometry("400x300")
        ventana_acerca.config(bg="#f0f0f0")
        tk.Label(ventana_acerca, text="Programa elaborado como Proyecto Airbnb").pack(pady=20)
        tk.Label(ventana_acerca, text="Desarrollado por Antony Cervantes Calderon").pack(pady=20)
        tk.Label(ventana_acerca, text="II Cuatrimestre 2025").pack(pady=20)
    
    
    def ventanaEditarCliente(self):
        EditarCliente(master=self.ventana, email=self.email,contrasena=self.contrasena) #Recibe el email y contrasena, para que el cliente solo vea su perfil y no el de los demas  

    def ventanaEliminarCliente(self):
        EliminarCliente(master=self.ventana, email=self.email,contrasena=self.contrasena)
    

    def ventanaRegistrarReserva (self):
        RegistrarReservacion(self.ventana)
    
    def ventanaEditarReserva(self):
        EditarReservacion(self.ventana)

    def ventanaEliminarReserva(self):
        EliminarReservacion(self.ventana)
