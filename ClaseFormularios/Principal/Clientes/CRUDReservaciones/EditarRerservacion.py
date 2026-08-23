import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter.font import BOLD
from datetime import datetime
from ClasesNegocios.Propiedades import Propiedades
from ClasesNegocios.Reservas import Reservas


class EditarReservacion(tk.Toplevel): 

    def __init__(self, master=None):
        super().__init__(master)
        self.precio = 0
        self.title("Editar Reservacion")
        w, h = self.winfo_screenwidth(), self.winfo_screenheight()
        self.geometry("%dx%d+0+0" % (w,h))
        self.config(bg="#fcfcfc")
        self.resizable(True, True)
        self.state("zoomed")

        label = tk.Label(self)
        label.place(x=0, y=0, relwidth=1, relheight=1)

        columnas=("col1","col2","col3","col4","col5","col6","col7")
        self.tabla = ttk.Treeview(self,columns=columnas)
        self.tabla.grid(row=1,column=0, columnspan=8)

        self.tabla.heading("col1", text="IDENTIFICACION_DEL_CLIENTE")
        self.tabla.heading("col2", text="ID_SITIO")
        self.tabla.heading("col3", text= "FECHA_DE_ENTRADA")
        self.tabla.heading("col4", text= "FECHA_DE_SALIDA")
        self.tabla.heading("col5", text= "DISPONIBILIDAD")
        self.tabla.heading("col6", text="PERSONA_A_IR")
        self.tabla.heading("col7", text="TOTAL")
        self.tabla["show"] = "headings"
        self.tabla.bind("<ButtonRelease-1>", self.seleccionarReservacionTabla)


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

        self.btn_registrar = tk.Button(self, text="Editar Reservacion", command= self.editarReservacion, bg="#666a88", fg="#fcfcfc")
        self.btn_registrar.grid(row=8, columnspan=2, sticky=("W"))

        self.mostrarReservacion()

    def limpiarCampos(self):
        self.txt_id.delete(0, tk.END)
        self.txt_id_sitio.delete(0, tk.END)
        self.txt_fecha_entrada.delete(0, tk.END)
        self.txt_fecha_salida.delete(0, tk.END)
        self.txt_cantidad_personas.delete(0, tk.END)

    def mostrarReservacion(self):

        reservacion = Reservas()
        reservaciones = reservacion.leer_reserva()

        for item in self.tabla.get_children():
            self.tabla.delete(item)

        for reserva in reservaciones:
            self.tabla.insert("",tk.END, values=(
                reserva.get("Identificacion del cliente",""),
                reserva.get("ID Sitio",""),
                reserva.get("Fecha de entrada",""),
                reserva.get("Fecha de salida", ""),
                reserva.get("Disponibilidad",""),
                reserva.get("Cantidad de personas",""),
                reserva.get("Total", "")
            ))

    def seleccionarReservacionTabla(self, event):
        item = self.tabla.focus()
        if item:
            valores = self.tabla.item(item, "values")
            self.txt_id.delete(0, tk.END)
            self.txt_id.insert(0, valores[0])
            self.txt_id_sitio.delete(0, tk.END)
            self.txt_id_sitio.insert(0, valores[1])
            self.txt_fecha_entrada.delete(0, tk.END)
            self.txt_fecha_entrada.insert(0, valores[2])
            self.txt_fecha_salida.delete(0, tk.END)
            self.txt_fecha_salida.insert(0, valores[3])
            self.txt_cantidad_personas.delete(0, tk.END)
            self.txt_cantidad_personas.insert(0, valores[5])

    def editarReservacion(self):        
        try:
            reservaciones = Reservas()
            propiedad = Propiedades()
            identificacion = int(self.txt_id.get())
            id_sitio = int(self.txt_id_sitio.get())
            fecha_entrada = self.txt_fecha_entrada.get()
            fecha_salida = self.txt_fecha_salida.get()
            cantidad_personas = int(self.txt_cantidad_personas.get())
            self.precio = propiedad.buscar_precio(id_sitio)
            disponible = "No"

            if reservaciones.editar_reserva(identificacion, id_sitio, fecha_entrada, fecha_salida,disponible, cantidad_personas, self.precio):
                messagebox.showinfo("Éxito", "La reservació se edito correctamente.")
                self.mostrarReservacion()
                self.limpiarCampos()

        except Exception as e:
            messagebox.showerror(message=str(e), title="Ha ocurrido un error:")
            self.destroy()


