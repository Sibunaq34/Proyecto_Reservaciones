import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from ClasesNegocios.Reservas import Reservas


class EliminarReservacion(tk.Toplevel): 

    def __init__(self, master=None):
        super().__init__(master)
        self.precio = 0
        self.title("Eliminar Reservacion")
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

        self.tabla.heading("col1", text="ID de la Reservacion")
        self.tabla.heading("col2", text="ID del Sitio")
        self.tabla.heading("col3", text= "Fecha de entrada")
        self.tabla.heading("col4", text= "Fecha de salida")
        self.tabla.heading("col5", text= "Disponibilidad")
        self.tabla.heading("col6", text="Cantidad de personas")
        self.tabla.heading("col7", text="Total")
        self.tabla["show"] = "headings"
        self.tabla.bind("<ButtonRelease-1>", self.seleccionarReservacionTabla)


        lblid = tk.Label(self, text="ID de la reservacion:",font=("Times", 14), fg="#666a88", anchor="w")
        lblid.grid(row=2,column=0, sticky="W")
        self.txt_id = tk.Entry(self)
        self.txt_id.grid(row=2,column=1, sticky="W")

        self.btn_registrar = tk.Button(self, text="Eliminar Reservacion", command= self.eliminarReservacion, bg="#666a88", fg="#fcfcfc")
        self.btn_registrar.grid(row=8, columnspan=2, sticky=("W"))

        self.mostrarReservacion()


    def limpiarCampos(self):
        self.txt_id.delete(0, tk.END)


    def mostrarReservacion(self):

        reservaciones = Reservas()
        reservaciones = reservaciones.leer_reserva()

        for item in self.tabla.get_children():
            self.tabla.delete(item)

        for reserva in reservaciones:
            self.tabla.insert("",tk.END, values=(
                reserva.get("ID de la Reservacion",""),
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


    def eliminarReservacion(self):        
        try:
            reservaciones = Reservas()
            identificacion = int(self.txt_id.get())

            if reservaciones.eliminar_reserva(identificacion):
                messagebox.showinfo("Éxito", "Reservación eliminada correctamente.")
                self.mostrarReservacion()
                self.limpiarCampos()

        except Exception as e:
            messagebox.showerror(message=str(e), title="Ha ocurrido un error:")
            self.destroy()
