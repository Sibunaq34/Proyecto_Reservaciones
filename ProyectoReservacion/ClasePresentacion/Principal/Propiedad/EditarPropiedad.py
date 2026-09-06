import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter.font import BOLD
from ClasesNegocios.Propiedades import Propiedades

class EditarPropiedades(tk.Toplevel): 

    def __init__(self, master=None):
        super().__init__(master)
        self.title("Editar Propiedad")
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

        self.tabla.heading("col1", text="ID del sitio")
        self.tabla.heading("col2", text="Tipo De Propiedad")
        self.tabla.heading("col3", text= "Ubicacion")
        self.tabla.heading("col4", text= "Cantidad maxima de personas")
        self.tabla.heading("col5", text= "Precio por noche")
        self.tabla.heading("col6", text="Contacto")
        self.tabla["show"] = "headings"

        self.tabla.bind("<ButtonRelease-1>", self.seleccionarPropiedadesTabla)

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
        
        self.btn_registrar = tk.Button(self, text="Registrar Propiedad", command= self.editar_propiedades, bg="#666a88", fg="#fcfcfc")
        self.btn_registrar.grid(row=10, columnspan=2, sticky=("W"))
        self.mostrarDatos()


    def limpiarCampos(self):
        self.txt_id_sitio.delete(0, tk.END)
        self.txt_tipo_propie.delete(0, tk.END)
        self.txt_ubicacion.delete(0, tk.END)
        self.txt_cantidad_maxima_personas.delete(0, tk.END)
        self.txt_precio_noche.delete(0, tk.END)
        self.txt_contacto.delete(0, tk.END)

    def mostrarDatos(self):

        propiedades= Propiedades()
        propiedades = propiedades.leer_propiedades()

        for item in self.tabla.get_children():
            self.tabla.delete(item)

        for propiedad in propiedades:
            self.tabla.insert("",tk.END, values=(
                propiedad.get("ID del sitio",""),
                propiedad.get("Tipo de Propiedad",""),
                propiedad.get("Ubicacion",""),
                propiedad.get("Cantidad maxima de personas", ""),
                propiedad.get("Precio por noche",""),
                propiedad.get("Contacto", "")
            ))
    
    def seleccionarPropiedadesTabla(self, event):
        item = self.tabla.focus()
        if item:
            valores = self.tabla.item(item, "values")
            self.txt_id_sitio.delete(0, tk.END)
            self.txt_id_sitio.insert(0, valores[0])
            self.txt_tipo_propie.delete(0, tk.END)
            self.txt_tipo_propie.insert(0, valores[1])
            self.txt_ubicacion.delete(0, tk.END)
            self.txt_ubicacion.insert(0, valores[2])
            self.txt_cantidad_maxima_personas.delete(0, tk.END)
            self.txt_cantidad_maxima_personas.insert(0, valores[3])
            self.txt_precio_noche.delete(0, tk.END)
            self.txt_precio_noche.insert(0, valores[4])
            self.txt_contacto.delete(0, tk.END)
            self.txt_contacto.insert(0, valores[5])

    
    def editar_propiedades (self):

        try:
            propiedad = Propiedades()
            propiedad= propiedad.editar_propiedad(self.txt_id_sitio.get(),self.txt_tipo_propie.get(), self.txt_ubicacion.get(),int(self.txt_cantidad_maxima_personas.get()), int(self.txt_precio_noche.get()),int(self.txt_contacto.get()))
            if propiedad:
                self.mostrarDatos()
                self.limpiarCampos()

        except Exception as e:
            messagebox.showerror(message=str(e),title="Ha ocurrido un error:")
            self.destroy()











