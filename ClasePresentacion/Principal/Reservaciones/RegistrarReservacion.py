import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter.font import BOLD
from ClasesNegocios.Propiedades import Propiedades
from ClasesNegocios.Usuarios import Usuarios
from ClasesNegocios.Reservas import Reservas


class RegistrarReservacion(tk.Toplevel): 

    def __init__(self, master=None):
        super().__init__(master)
        self.precio = 0
        self.title("Registrar Reservacion")
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
        self.tabla.bind("<ButtonRelease-1>", self.seleccionarPropiedadesTabla)


        lblid = tk.Label(self, text="Identificacion:",font=("Times", 14), fg="#666a88", anchor="w")
        lblid.grid(row=2,column=0, sticky="W")
        self.txt_id = tk.Entry(self)
        self.txt_id.grid(row=2,column=1, sticky="W")

        lbl_id_sitio = tk.Label(self, text="ID del sitio:",font=("Times", 14), fg="#666a88", anchor="w")
        lbl_id_sitio.grid(row=3,column=0, sticky="W")
        self.txt_id_sitio= tk.Entry(self)
        self.txt_id_sitio.grid(row=3,column=1, sticky="W")

        lbl_fecha_entrada = tk.Label(self, text="Fecha de entrada:",font=("Times", 12), fg="#666a88", anchor="w")
        lbl_fecha_entrada.grid(row=4,column=0, sticky="W")
        self.txt_fecha_entrada= tk.Entry(self)
        self.txt_fecha_entrada.grid(row=4,column=1, sticky="W")

        lbl_fecha_salida = tk.Label(self, text="Fecha de salida:",font=("Times", 12), fg="#666a88", anchor="w")
        lbl_fecha_salida.grid(row=5,column=0, sticky="W")
        self.txt_fecha_salida = tk.Entry(self)
        self.txt_fecha_salida.grid(row=5,column=1, sticky="W")
        
        lbl_cantidad_personas = tk.Label(self, text="Cantidad de personas a ir:",font=("Times", 12), fg="#666a88", anchor="w")
        lbl_cantidad_personas.grid(row=6,column=0, sticky="W")
        self.txt_cantidad_personas = tk.Entry(self)
        self.txt_cantidad_personas.grid(row=6,column=1, sticky="W")

        lbl_precio_noche = tk.Label(self, text="Precio por noche:",font=("Times", 12), fg="#666a88", anchor="w")
        lbl_precio_noche.grid(row=7,column=0, sticky="W")
        self.lbl_precio_noche = tk.Label(self, text=str(self.precio),font=("Times", 12), fg="#666a88", anchor="w")
        self.lbl_precio_noche.grid(row=7,column=1, sticky="W")

        self.btn_registrar = tk.Button(self, text="Realizar Reservacion", command= self.registra_reservacion, bg="#666a88", fg="#fcfcfc")
        self.btn_registrar.grid(row=8, columnspan=2, sticky=("W"))

        self.mostrarPropiedades()

    def limpiarCampos(self):
        self.txt_id.delete(0, tk.END)
        self.txt_id_sitio.delete(0, tk.END)
        self.txt_fecha_entrada.delete(0, tk.END)
        self.txt_fecha_salida.delete(0, tk.END)
        self.txt_cantidad_personas.delete(0, tk.END)

    def mostrarPropiedades(self):

        propiedades = Propiedades()
        propiedades= propiedades.leer_propiedades()

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
            self.precio = int(valores[4])


    def registra_reservacion(self):

        try:
            cliente = Usuarios()
            if self.txt_id.get() and self.txt_id_sitio.get() and self.txt_fecha_entrada.get() and self.txt_fecha_salida.get() and self.txt_cantidad_personas.get():
                identificacion = int(self.txt_id.get())
                tipo = "Cliente"
                usuarios = cliente.validar_usuario(tipo, identificacion)
                if usuarios:
                    reservacion = Reservas()
                    id_sitio = int(self.txt_id_sitio.get())
                    fecha_entrada = self.txt_fecha_entrada.get()
                    fecha_salida = self.txt_fecha_salida.get()
                    reserva_existente = reservacion.validacion_fecha(id_sitio, fecha_entrada, fecha_salida)
                    if reserva_existente:
                        messagebox.showwarning(title="Reservacion",
                                               message="Ya existe una reservacion para esas fechas en esta propiedad.")
                        return
                    cantidad_personas = int(self.txt_cantidad_personas.get())
                    disponible = "No"
                    reservacion.registrar_reserva(identificacion, id_sitio, fecha_entrada, fecha_salida, disponible,
                                                  cantidad_personas, self.precio)
                    self.mostrarPropiedades()
                    self.limpiarCampos()
                else:
                    messagebox.showerror(title="Error", message="La identificacion no esta registrada como cliente")
                    return
            else:
                messagebox.showerror(title="Error", message="Error, los campos no pueden estar vacios")
                return
        except Exception as e:
            messagebox.showerror(message=str(e), title="Ha ocurrido un error:")
            self.destroy()





