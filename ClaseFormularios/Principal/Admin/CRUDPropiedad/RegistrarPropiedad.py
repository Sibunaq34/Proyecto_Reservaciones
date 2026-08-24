import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter.font import BOLD
from ClasesDatos.Dueno import ArchivoDuenos
from ClasesNegocios.Propiedades import Propiedades


class RegistrarPropiedad(tk.Toplevel): 

    def __init__(self, master=None):
        super().__init__(master)
        self.title("Registrar Propiedad")
        w, h = self.winfo_screenwidth(), self.winfo_screenheight()
        self.geometry("%dx%d+0+0" % (w,h))
        self.config(bg="#fcfcfc")
        self.resizable(True, True)
        self.state("zoomed")

        label = tk.Label(self)
        label.place(x=0, y=0, relwidth=1, relheight=1)

        columnas=("col1","col2","col3","col4","col5","col6","col7" )
        self.tabla = ttk.Treeview(self,columns=columnas)
        self.tabla.grid(row=1,column=0, columnspan=7)

        self.tabla.heading("col1", text="Identificacion")
        self.tabla.heading("col2", text="ID del sitio")
        self.tabla.heading("col3", text="Tipo De Propiedad")
        self.tabla.heading("col4", text= "Ubicacion")
        self.tabla.heading("col5", text= "Cantidad maxima de personas")
        self.tabla.heading("col6", text= "Precio por noche")
        self.tabla.heading("col7", text="Contacto")
        self.tabla["show"] = "headings"

        lblid = tk.Label(self, text="Identificacion:",font=("Times", 14), fg="#666a88", anchor="w")
        lblid.grid(row=2,column=0, sticky="W")
        self.txt_id = tk.Entry(self)
        self.txt_id.grid(row=2,column=1, sticky="W")

        lblid_sitio = tk.Label(self, text="ID del sitio:",font=("Times", 14), fg="#666a88", anchor="w")
        lblid_sitio.grid(row=3,column=0, sticky="W")
        self.txt_id_sitio= tk.Entry(self)
        self.txt_id_sitio.grid(row=3,column=1, sticky="W")

        lbl_tipo_propie = tk.Label(self, text="Tipo de propiedad:",font=("Times", 12), fg="#666a88", anchor="w")
        lbl_tipo_propie.grid(row=4,column=0, sticky="W")
        self.txt_tipo_propie= tk.Entry(self)
        self.txt_tipo_propie.grid(row=4,column=1, sticky="W")

        lbl_ubicacion = tk.Label(self, text="Ubicacion:",font=("Times", 12), fg="#666a88", anchor="w")
        lbl_ubicacion.grid(row=5,column=0, sticky="W")
        self.txt_ubicacion = tk.Entry(self)
        self.txt_ubicacion.grid(row=5,column=1, sticky="W")
        
        lbl_cantidad_maxima_personas = tk.Label(self, text="Cantidad maxima de personas permitidas",font=("Times", 12), fg="#666a88", anchor="w")
        lbl_cantidad_maxima_personas.grid(row=7,column=0, sticky="W")
        self.txt_cantidad_maxima_personas = tk.Entry(self)
        self.txt_cantidad_maxima_personas.grid(row=7,column=1, sticky="W")

        lbl_precio_noche = tk.Label(self, text="Precio por noche:",font=("Times", 12), fg="#666a88", anchor="w")
        lbl_precio_noche.grid(row=8,column=0, sticky="W")
        self.txt_precio_noche = tk.Entry(self)
        self.txt_precio_noche.grid(row=8,column=1, sticky="W")

        lbl_contacto = tk.Label(self, text="Numero de telefono:",font=("Times", 12), fg="#666a88", anchor="w")
        lbl_contacto.grid(row=9,column=0, sticky="W")
        self.txt_contacto = tk.Entry(self)
        self.txt_contacto.grid(row=9,column=1, sticky="W")
        
        self.btn_registrar = tk.Button(self, text="Registrar Propiedad", command= self.registrar_propiedad, bg="#666a88", fg="#fcfcfc")
        self.btn_registrar.grid(row=10, columnspan=2, sticky=("W"))
        self.mostrarDatos()

    def limpiarCampos(self):
        self.txt_id.delete(0, tk.END)
        self.txt_tipo_propie.delete(0, tk.END)
        self.txt_ubicacion.delete(0, tk.END)
        self.txt_cantidad_maxima_personas.delete(0, tk.END)
        self.txt_precio_noche.delete(0, tk.END)
        self.txt_contacto.delete(0, tk.END)

    def mostrarDatos(self):

        propiedades= Propiedades.leer_propiedades()

        propiedades = propiedades["propiedades"]["usuario"]
        for item in self.tabla.get_children():
            self.tabla.delete(item)

        for propiedad in propiedades:
            self.tabla.insert("",tk.END, values=(
                propiedad.get("Identificacion",""),
                propiedad.get("ID del sitio",""),
                propiedad.get("Tipo de Propiedad",""),
                propiedad.get("Ubicacion",""),
                propiedad.get("Cantidad maxima de personas", ""),
                propiedad.get("Precio por noche",""),
                propiedad.get("Contacto", "")
            ))
    
    def registrar_propiedad (self):

        try:
            dueno= ArchivoDuenos()
            if self.txt_id.get() and self.txt_id_sitio.get() and self.txt_tipo_propie.get() and self.txt_ubicacion.get() and self.txt_cantidad_maxima_personas.get() and self.txt_precio_noche.get() and self.txt_contacto.get():
                identificacion = int(self.txt_id.get())
                usuarios = dueno.validacionDueno(identificacion)
                if usuarios:
                    id_sitio = self.txt_id_sitio.get()
                    tipo_propie = self.txt_tipo_propie.get()
                    ubicacion = self.txt_ubicacion.get()
                    cantidad_maxima = int(self.txt_cantidad_maxima_personas.get())
                    precio_noche = int(self.txt_precio_noche.get())
                    contacto = self.txt_contacto.get()

                    propiedad= Propiedades(identificacion, id_sitio, tipo_propie, ubicacion, cantidad_maxima, precio_noche, contacto)
                    propiedad.registrar_propiedad()
                    self.mostrarDatos()
                    self.limpiarCampos() 
                else:
                    messagebox.showerror(title="Error", message="La identificacion no esta registrada como dueño")
                    self.destroy()
            else:
                messagebox.showerror("Error, los campos no pueden estar vacios")
                self.destroy()
        except Exception as e:
            messagebox.showerror(message=str(e),title="Ha ocurrido un error:")
            self.destroy()










