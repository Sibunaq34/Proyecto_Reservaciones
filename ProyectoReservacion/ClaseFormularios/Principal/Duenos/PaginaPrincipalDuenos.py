import tkinter as tk
from tkinter.font import BOLD
from ClaseFormularios.Principal.Duenos.CRUDDuenos.EditarDuenos import *
from ClaseFormularios.Principal.Duenos.CRUDDuenos.EliminarDuenos import *

from ClaseFormularios.Principal.Duenos.CRUDPropiedad.RegistrarPropiedad import *
from ClaseFormularios.Principal.Duenos.CRUDPropiedad.EditarPropiedad import *
from ClaseFormularios.Principal.Duenos.CRUDPropiedad.EliminarPropiedad import *

class PaginaPrincipalDuenos: 
    
    def __init__(self, email, contrasena):
        self.ventana = tk.Tk()
        self.email = email
        self.contrasena = contrasena
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

        menu_duenos = tk.Menu(MSmenu, tearoff=0) #Crea la bandeja del menu
        menu_propiedades = tk.Menu(MSmenu, tearoff=0) 
        MSmenu.add_cascade(label="Perfil", menu=menu_duenos) #Agrega las opciones principales esto con el add cascade
        MSmenu.add_cascade(label="Propiedades", menu=menu_propiedades) #Agrega las opciones principales esto con el add cascade
        MSmenu.add_cascade(label="Acerca de", command=self.acerca_de)
        MSmenu.add_cascade(label="Salir", command=self.ventana.destroy)

        
        menu_duenos.add_command(label="Editar cuenta", command=self.ventanaEditarDueno)
        menu_duenos.add_command(label="Eliminar cuenta", command=self.ventanaEliminarDueno)

        menu_propiedades.add_command(label="Registrar", command=self.ventanaRegistraPropiedad) #Agrega las opciones que estaran en el boton de Clientes generado por MSmenu, mas genera la accion para el boton
        menu_propiedades.add_command(label="Editar", command=self.ventanaEditarPropiedad)
        menu_propiedades.add_command(label="Eliminar", command=self.ventanaEliminarPropiedad)

        self.ventana.mainloop()
    
    def acerca_de(self):
        ventana_acerca = tk.Toplevel(self.ventana)
        ventana_acerca.title("Acerca de")
        ventana_acerca.geometry("400x300")
        ventana_acerca.config(bg="#f0f0f0")
        tk.Label(ventana_acerca, text="Programa elaborado como Proyecto Airbnb").pack(pady=20)
        tk.Label(ventana_acerca, text="Desarrollado por Antony Cervantes Calderon").pack(pady=20)
        tk.Label(ventana_acerca, text="II Cuatrimestre 2025").pack(pady=20)
    

    
    def ventanaEditarDueno(self):
        EditarDuenos(master=self.ventana, email=self.email, contrasena=self.contrasena)

    def ventanaEliminarDueno(self):
        EliminarDueno(master=self.ventana, email=self.email, contrasena=self.contrasena)


    def ventanaRegistraPropiedad (self):
        RegistrarPropiedad(self.ventana)
    
    def ventanaEditarPropiedad(self):
        EditarPropiedades(self.ventana)

    def ventanaEliminarPropiedad(self):
        EliminarPropiedades(self.ventana)
