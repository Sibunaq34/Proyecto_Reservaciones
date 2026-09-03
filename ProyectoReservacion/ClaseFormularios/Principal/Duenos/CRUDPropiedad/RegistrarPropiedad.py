import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter.font import BOLD
from ClasesDatos.JsonPropiedad import JsonPropiedad
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

        columnas=("col1","col2","col3","col4","col5","col6")
        self.tabla = ttk.Treeview(self,columns=columnas)
        self.tabla.grid(row=1,column=0, columnspan=7)

        self.tabla.heading("col1", text="ID")
        self.tabla.heading("col2", text="Tipo_De_Propiedad")
        self.tabla.heading("col3", text= "UBICACION")
        self.tabla.heading("col4", text= "CANTIDAD_MAXIMA_PERSONAS")
        self.tabla.heading("col5", text= "PRECIO_POR_NOCHE")
        self.tabla.heading("col6", text="CONTACTO")
        self.tabla["show"] = "headings"

        lblid = tk.Label(self, text="ID:",font=("Times", 14), fg="#666a88", anchor="w")
        lblid.grid(row=2,column=0, sticky="W")
        self.txt_id = tk.Entry(self)
        self.txt_id.grid(row=2,column=1, sticky="W")

        lbl_tipo_propie = tk.Label(self, text="Tipo de propiedad:",font=("Times", 12), fg="#666a88", anchor="w")
        lbl_tipo_propie.grid(row=3,column=0, sticky="W")
        self.txt_tipo_propie= tk.Entry(self)
        self.txt_tipo_propie.grid(row=3,column=1, sticky="W")

        lbl_ubicacion = tk.Label(self, text="Ubicacion:",font=("Times", 12), fg="#666a88", anchor="w")
        lbl_ubicacion.grid(row=4,column=0, sticky="W")
        self.txt_ubicacion = tk.Entry(self)
        self.txt_ubicacion.grid(row=4,column=1, sticky="W")
        
        lbl_cantidad_maxima_personas = tk.Label(self, text="Cantidad maxima de personas permitidas",font=("Times", 12), fg="#666a88", anchor="w")
        lbl_cantidad_maxima_personas.grid(row=5,column=0, sticky="W")
        self.txt_cantidad_maxima_personas = tk.Entry(self)
        self.txt_cantidad_maxima_personas.grid(row=5,column=1, sticky="W")

        lbl_precio_noche = tk.Label(self, text="Precio por noche:",font=("Times", 12), fg="#666a88", anchor="w")
        lbl_precio_noche.grid(row=6,column=0, sticky="W")
        self.txt_precio_noche = tk.Entry(self)
        self.txt_precio_noche.grid(row=6,column=1, sticky="W")

        lbl_contacto = tk.Label(self, text="Numero de telefono:",font=("Times", 12), fg="#666a88", anchor="w")
        lbl_contacto.grid(row=7,column=0, sticky="W")
        self.txt_contacto = tk.Entry(self)
        self.txt_contacto.grid(row=7,column=1, sticky="W")
        
        self.btn_registrar = tk.Button(self, text="Registrar Propiedad", command= self.registrarPropiedad, bg="#666a88", fg="#fcfcfc")
        self.btn_registrar.grid(row=8, columnspan=2, sticky=("W"))
        self.mostrarDatos()

    def limpiarCampos(self):
        self.txt_id.delete(0, tk.END)
        self.txt_tipo_propie.delete(0, tk.END)
        self.txt_ubicacion.delete(0, tk.END)
        self.txt_cantidad_maxima_personas.delete(0, tk.END)
        self.txt_precio_noche.delete(0, tk.END)
        self.txt_contacto.delete(0, tk.END)

    def mostrarDatos(self):

        jsonpropiedad = JsonPropiedad()
        propiedades= jsonpropiedad.leerPropiedades()

        for item in self.tabla.get_children():
            self.tabla.delete(item)

        for propiedad in propiedades:
            self.tabla.insert("",tk.END, values=(
                propiedad.get("ID:",""),
                propiedad.get("Tipo de Propiedad:",""),
                propiedad.get("Ubicacion:",""),
                propiedad.get("Cantidad maxima de personas:", ""),
                propiedad.get("Precio por noche:",""),
                propiedad.get("Contacto:", "")
            ))
    
    def registrarPropiedad (self):

        jsonpropiedad = JsonPropiedad()
        try:
            dueno= ArchivoDuenos()
            if self.txt_id.get() and self.txt_tipo_propie.get() and self.txt_ubicacion.get() and self.txt_cantidad_maxima_personas.get() and self.txt_precio_noche.get() and self.txt_contacto.get():
                identificacion = int(self.txt_id.get())
                usuarios = dueno.validacionDueno(identificacion)
                if usuarios:
                    tipo_propie = self.txt_tipo_propie.get()
                    ubicacion = self.txt_ubicacion.get()
                    cantidad_maxima = int(self.txt_cantidad_maxima_personas.get())
                    precio_noche = int(self.txt_precio_noche.get())
                    contacto = int(self.txt_contacto.get())

                    propiedad = Propiedades(identificacion, tipo_propie, ubicacion, cantidad_maxima, precio_noche, contacto)

                    jsonpropiedad.RegistrarPropiedad(propiedad)

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










