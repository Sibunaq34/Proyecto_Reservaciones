import tkinter as tk
from tkinter.font import BOLD
from ClaseFormularios.Principal.Admin.CRUDDuenos.EditarDuenos import *
from ClaseFormularios.Principal.Admin.CRUDDuenos.EliminarDuenos import *
from ClaseFormularios.Principal.Admin.CRUDDuenos.RegistrarDuenos import *

from ClaseFormularios.Principal.Admin.CRUDClientes.EditarCliente import *
from ClaseFormularios.Principal.Admin.CRUDClientes.EliminarCliente import *
from ClaseFormularios.Principal.Admin.CRUDClientes.RegistrarCliente import *

from ClaseFormularios.Principal.Admin.CRUDPropiedad.RegistrarPropiedad import *
from ClaseFormularios.Principal.Admin.CRUDPropiedad.EditarPropiedad import *
from ClaseFormularios.Principal.Admin.CRUDPropiedad.EliminarPropiedad import *

from ClaseFormularios.Principal.Admin.CRUDReservaciones.RegistrarReservacion import *
from ClaseFormularios.Principal.Admin.CRUDReservaciones.EliminarReservacion import *
from ClaseFormularios.Principal.Admin.CRUDReservaciones.EditarRerservacion import *

class PaginaPrincipal: 
    
    def __init__(self):
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

        #region Menu Strip
        menu_clientes = tk.Menu(MSmenu, tearoff=0) #Crea la bandeja del menu
        menu_duenos = tk.Menu(MSmenu, tearoff=0)
        menu_propiedades = tk.Menu(MSmenu, tearoff=0) 
        menu_reservaciones = tk.Menu(MSmenu, tearoff=0) 
        MSmenu.add_cascade(label="Clientes", menu=menu_clientes)  #Agrega las opciones principales esto con el add cascade
        MSmenu.add_cascade(label="Dueños", menu=menu_duenos)
        MSmenu.add_cascade(label="Propiedades", menu=menu_propiedades)
        MSmenu.add_cascade(label="Reservaciones", menu=menu_reservaciones)
        MSmenu.add_cascade(label="Acerca de", command=self.acerca_de)
        MSmenu.add_cascade(label="Salir", command=self.ventana.destroy)
        #endregion


        #region Submenu Cliente
        menu_clientes.add_command(label="Registrar", command=self.ventanaRegistraCliente) #Agrega las opciones que estaran en el boton de Clientes generado por MSmenu, mas genera la accion para el boton
        menu_clientes.add_command(label="Editar", command=self.ventanaEditarCliente)
        menu_clientes.add_command(label="Eliminar", command=self.ventanaEliminarCliente)
        #endregion


        #region Submenu Dueno
        menu_duenos.add_command(label="Registrar", command=self.ventanaRegistraDueno) #Agrega las opciones que estaran en el boton de Clientes generado por MSmenu, mas genera la accion para el boton
        menu_duenos.add_command(label="Editar", command=self.ventanaEditarDueno)
        menu_duenos.add_command(label="Eliminar", command=self.ventanaEliminarDueno)
        #endregion


        #region Submenu propiedad
        menu_propiedades.add_command(label="Registrar", command=self.ventanaRegistrarPropiedad) #Agrega las opciones que estaran en el boton de Clientes generado por MSmenu, mas genera la accion para el boton
        menu_propiedades.add_command(label="Editar", command=self.ventanaEditarPropiedades)
        menu_propiedades.add_command(label="Eliminar", command=self.ventanaEliminarPropiedad)
        #endregion


        #region Submenu Reservas
        menu_reservaciones.add_command(label="Registrar", command=self.ventanaRegistrarReserva) #Agrega las opciones que estaran en el boton de Clientes generado por MSmenu, mas genera la accion para el boton
        menu_reservaciones.add_command(label="Editar", command=self.ventanaEditarReserva)
        menu_reservaciones.add_command(label="Eliminar", command=self.ventanaEliminarReserva)
        self.ventana.mainloop()
        #endregion


    def acerca_de(self):
        ventana_acerca = tk.Toplevel(self.ventana)
        ventana_acerca.title("Acerca de")
        ventana_acerca.geometry("400x300")
        ventana_acerca.config(bg="#f0f0f0")
        tk.Label(ventana_acerca, text="Programa elaborado como Proyecto Airbnb").pack(pady=20)
        tk.Label(ventana_acerca, text="Desarrollado por Antony Cervantes Calderon").pack(pady=20)
        tk.Label(ventana_acerca, text="II Cuatrimestre 2025").pack(pady=20)
    

    def ventanaRegistraCliente (self):
        RegistrarUsuario(self.ventana)
    
    def ventanaEditarCliente(self):
        EditarCliente(self.ventana)

    def ventanaEliminarCliente(self):
        EliminarCliente(self.ventana)


#region ventana CRUD de dueños
    def ventanaRegistraDueno (self):
        RegistrarDueno(self.ventana)
    
    def ventanaEditarDueno(self):
        EditarDuenos(self.ventana)

    def ventanaEliminarDueno(self):
        EliminarDueno(self.ventana)
#endregion


#region ventana CRUD de propiedades
    def ventanaRegistrarPropiedad (self):
        RegistrarPropiedad(self.ventana)
    
    def ventanaEditarPropiedades(self):
        EditarPropiedades(self.ventana)

    def ventanaEliminarPropiedad(self):
        EliminarPropiedades(self.ventana)
#endregion


#region ventana CRUD de Reservaciones
    def ventanaRegistrarReserva (self):
        RegistrarReservacion(self.ventana)
    
    def ventanaEditarReserva(self):
        EditarReservacion(self.ventana)

    def ventanaEliminarReserva(self):
        EliminarReservacion(self.ventana)
#endregion