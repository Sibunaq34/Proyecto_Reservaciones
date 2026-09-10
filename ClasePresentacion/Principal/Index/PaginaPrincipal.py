
from ClasePresentacion.Principal.Usuario.EditarUsuario import *
from ClasePresentacion.Principal.Usuario.EliminarUsuario import *
from ClasePresentacion.Principal.Usuario.RegistrarUsuario import *

from ClasePresentacion.Principal.Propiedad.RegistrarPropiedad import *
from ClasePresentacion.Principal.Propiedad.EditarPropiedad import *
from ClasePresentacion.Principal.Propiedad.EliminarPropiedad import *

from ClasePresentacion.Principal.Reservaciones.RegistrarReservacion import *
from ClasePresentacion.Principal.Reservaciones.EliminarReservacion import *
from ClasePresentacion.Principal.Reservaciones.EditarRerservacion import *

class PaginaPrincipal: 
    
    def __init__(self, tipo, identificacion):
        self.tipo = tipo
        self.identificacion = identificacion
        self.ventana = tk.Tk()
        self.ventana.title("Paginal Principal")
        w, h = self.ventana.winfo_screenwidth(), self.ventana.winfo_screenheight()
        self.ventana.geometry("%dx%d+0+0" % (w, h))
        self.ventana.config(bg="#238799")
        self.ventana.resizable(True, True)
        self.ventana.state("zoomed")

        label = tk.Label(self.ventana)
        label.place(x=0, y=0, relwidth=1, relheight=1)
        
        ms_menu= tk.Menu(self.ventana)
        self.ventana.config(menu=ms_menu)

        #region Menu Strip
        menu_usuarios = tk.Menu(ms_menu, tearoff=0) #Crea la bandeja del menu
        menu_propiedades = tk.Menu(ms_menu, tearoff=0)
        menu_reservaciones = tk.Menu(ms_menu, tearoff=0)
        ms_menu.add_cascade(label="Usuario", menu=menu_usuarios)  #Agrega las opciones principales esto con el add cascade
        if self.tipo=="Dueno" or self.tipo == "Admin":
            ms_menu.add_cascade(label="Propiedades", menu=menu_propiedades)
        if self.tipo=="Cliente" or self.tipo== "Admin":
            ms_menu.add_cascade(label="Reservaciones", menu=menu_reservaciones)
        ms_menu.add_cascade(label="Acerca de", command=self.acerca_de)
        ms_menu.add_cascade(label="Salir", command=self.ventana.destroy)
        #endregion


        #region Submenu Cliente
        if self.tipo=="Admin":
            menu_usuarios.add_command(label="Registrar Usuario", command=self.ventana_registrar_usuario)
        if self.tipo == "Cliente" or self.tipo == "Admin":#Agrega las opciones que estaran en el boton de Usuario generado por MSmenu, mas genera la accion para el boton
            menu_reservaciones.add_command(label="Registrar",command=self.ventanar_registrar_reserva)  # Agrega las opciones que estaran en el boton de Usuario generado por MSmenu, mas genera la accion para el boton
            menu_reservaciones.add_command(label="Editar", command=self.ventana_editar_reserva)
            menu_reservaciones.add_command(label="Eliminar", command=self.ventana_eliminar_reserva)
        if self.tipo == "Dueno" or self.tipo=="Admin":
            menu_propiedades.add_command(label="Registrar", command=self.ventana_registrar_propiedad) #Agrega las opciones que estaran en el boton de Usuario generado por MSmenu, mas genera la accion para el boton
            menu_propiedades.add_command(label="Editar", command=self.ventanae_editar_propiedad)
            menu_propiedades.add_command(label="Eliminar", command=self.ventana_eliminar_propiedad)
        #endregion
        menu_usuarios.add_command(label="Editar", command=self.ventana_editar_usuario)
        menu_usuarios.add_command(label="Eliminar", command=self.ventana_eliminar_usuario)


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
    

    def  ventana_registrar_usuario(self):
        RegistrarUsuario(self.ventana)

    def ventana_editar_usuario(self):
        EditarCliente(self.ventana, self.tipo, self.identificacion)

    def ventana_eliminar_usuario(self):
        EliminarUsuario(self.ventana, self.tipo, self.identificacion)


    #region ventana CRUD de propiedades
    def ventana_registrar_propiedad (self):
        RegistrarPropiedad(self.ventana)

    def ventanae_editar_propiedad(self):
        EditarPropiedades(self.ventana)

    def ventana_eliminar_propiedad(self):
        EliminarPropiedades(self.ventana)
    #endregion


    #region ventana CRUD de Reservaciones
    def ventanar_registrar_reserva (self):
        RegistrarReservacion(self.ventana)

    def ventana_editar_reserva(self):
        EditarReservacion(self.ventana, self.tipo, self.identificacion)

    def ventana_eliminar_reserva(self):
        EliminarReservacion(self.ventana, self.tipo, self.identificacion)
#endregion