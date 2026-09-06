from ClasePresentacion.Principal.CRUDDuenos.EditarDuenos import *
from ClasePresentacion.Principal.CRUDDuenos.EliminarDuenos import *
from ClasePresentacion.Principal.CRUDDuenos.RegistrarDuenos import *

from ClasePresentacion.Principal.Clientes.EditarCliente import *
from ClasePresentacion.Principal.Clientes.EliminarCliente import *
from ClasePresentacion.Principal.Clientes.RegistrarCliente import *

from ClasePresentacion.Principal.Propiedad.RegistrarPropiedad import *
from ClasePresentacion.Principal.Propiedad.EditarPropiedad import *
from ClasePresentacion.Principal.Propiedad.EliminarPropiedad import *

from ClasePresentacion.Principal.Reservaciones.RegistrarReservacion import *
from ClasePresentacion.Principal.Reservaciones.EliminarReservacion import *
from ClasePresentacion.Principal.Reservaciones.EditarRerservacion import *

class PaginaPrincipal: 
    
    def __init__(self, tipo, email):
        self.tipo = tipo
        self.email = email
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
        menu_usuarios = tk.Menu(MSmenu, tearoff=0) #Crea la bandeja del menu
        menu_propiedades = tk.Menu(MSmenu, tearoff=0) 
        menu_reservaciones = tk.Menu(MSmenu, tearoff=0) 
        MSmenu.add_cascade(label="Usuario", menu=menu_usuarios)  #Agrega las opciones principales esto con el add cascade
        if self.tipo=="Dueno" or self.tipo == "Admin":
            MSmenu.add_cascade(label="Propiedades", menu=menu_propiedades)
        if self.tipo=="Cliente" or self.tipo== "Admin":
            MSmenu.add_cascade(label="Reservaciones", menu=menu_reservaciones)
        MSmenu.add_cascade(label="Acerca de", command=self.acerca_de)
        MSmenu.add_cascade(label="Salir", command=self.ventana.destroy)
        #endregion


        #region Submenu Cliente
        if self.tipo=="Admin":
            menu_usuarios.add_command(label="Registrar Cliente", command=self.ventana_registrar_cliente)
            menu_usuarios.add_command(label="Registrar Dueño", command=self.ventanaRegistraDueno)
        if self.tipo == "Cliente" or self.tipo == "Admin":#Agrega las opciones que estaran en el boton de Clientes generado por MSmenu, mas genera la accion para el boton
            menu_usuarios.add_command(label="Editar", command=self.ventana_editar_cliente)
            menu_usuarios.add_command(label="Eliminar", command=self.ventana_eliminar_cliente)
            menu_reservaciones.add_command(label="Registrar",command=self.ventanaRegistrarReserva)  # Agrega las opciones que estaran en el boton de Clientes generado por MSmenu, mas genera la accion para el boton
            menu_reservaciones.add_command(label="Editar", command=self.ventanaEditarReserva)
            menu_reservaciones.add_command(label="Eliminar", command=self.ventanaEliminarReserva)
        if self.tipo == "Dueno" or self.tipo=="Admin":
        # #Agrega las opciones que estaran en el boton de Clientes generado por MSmenu, mas genera la accion para el boton
            menu_usuarios.add_command(label="Editar", command=self.ventanaEditarDueno)
            menu_usuarios.add_command(label="Eliminar", command=self.ventana_eliminar_cliente)
        #region Submenu propiedad
            menu_propiedades.add_command(label="Registrar", command=self.ventanaRegistrarPropiedad) #Agrega las opciones que estaran en el boton de Clientes generado por MSmenu, mas genera la accion para el boton
            menu_propiedades.add_command(label="Editar", command=self.ventanaEditarPropiedades)
            menu_propiedades.add_command(label="Eliminar", command=self.ventanaEliminarPropiedad)
        #endregion


        #region Submenu Reservas
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
    

    def  ventana_registrar_cliente(self):
        RegistrarUsuario(self.ventana)

    def ventana_editar_cliente(self):
        EditarCliente(self.ventana)

    def ventana_eliminar_cliente(self):
        EliminarCliente(self.ventana, self.tipo, self.email)


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