import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from ClasesNegocios.Usuarios import Usuarios

class RegistrarUsuario(tk.Toplevel): 

    def __init__(self, master=None):
        super().__init__(master)
        self.title("Registrar Usuario")
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
        self.tabla.heading("col2", text="NOMBRE")
        self.tabla.heading("col3", text= "APELLIDOS")
        self.tabla.heading("col4", text= "EMAIL")
        self.tabla.heading("col5", text= "CONTRASENA")
        self.tabla.heading("col6", text="TIPO_DE_USUARIO")
        self.tabla["show"] = "headings"

        lblid = tk.Label(self, text="ID:",font=("Times", 14), fg="#666a88", anchor="w")
        lblid.grid(row=2,column=0, sticky="W")
        self.txt_id = tk.Entry(self)
        self.txt_id.grid(row=2,column=1, sticky="W")

        lbl_nombre = tk.Label(self, text="Nombre:",font=("Times", 12), fg="#666a88", anchor="w")
        lbl_nombre.grid(row=3,column=0, sticky="W")
        self.txt_nombre = tk.Entry(self)
        self.txt_nombre.grid(row=3,column=1, sticky="W")

        lbl_apellido = tk.Label(self, text="Apellidos:",font=("Times", 12), fg="#666a88", anchor="w")
        lbl_apellido.grid(row=4,column=0, sticky="W")
        self.txt_apellido = tk.Entry(self)
        self.txt_apellido.grid(row=4,column=1, sticky="W")
        
        lbl_email = tk.Label(self, text="Email:",font=("Times", 12), fg="#666a88", anchor="w")
        lbl_email.grid(row=5,column=0, sticky="W")
        self.txt_email = tk.Entry(self)
        self.txt_email.grid(row=5,column=1, sticky="W")

        lbl_contrasena = tk.Label(self, text="Contraseña:",font=("Times", 12), fg="#666a88", anchor="w")
        lbl_contrasena.grid(row=6,column=0, sticky="W")
        self.txt_contrasena = tk.Entry(self)
        self.txt_contrasena.grid(row=6,column=1, sticky="W")

        
        self.btn_registrar = tk.Button(self, text="Registrar Usuario", command= self.registrarUsuario, bg="#666a88", fg="#fcfcfc")
        self.btn_registrar.grid(row=8, columnspan=2, sticky=("W"))
        self.mostrarDatos()

    def limpiarCampos(self):
        self.txt_id.delete(0, tk.END)
        self.txt_nombre.delete(0, tk.END)
        self.txt_apellido.delete(0, tk.END)
        self.txt_email.delete(0, tk.END)
        self.txt_contrasena.delete(0, tk.END)

    def mostrarDatos(self):

        usuarios = Usuarios()
        usuarios= usuarios.leer_cliente()
        for usuario in usuarios:
            self.tabla.insert("",tk.END, values=(
                usuario.get("Identificacion", ""),
                usuario.get("Nombre",""),
                usuario.get("Apellidos",""),
                usuario.get("Email", ""),
                usuario.get("Contrasena",""),
                usuario.get("Tipo", "")
            ))
    
    def registrarUsuario (self):

        try:
            if self.txt_id.get() and self.txt_nombre.get() and self.txt_apellido.get() and self.txt_email.get() and self.txt_contrasena.get():
                cliente = Usuarios()
                identificacion = int(self.txt_id.get())
                nombre = self.txt_nombre.get()
                apellido = self.txt_apellido.get()
                email = self.txt_email.get()
                contrasena = self.txt_contrasena.get()
                tipo = "Cliente"
                cliente.registrar_usuario(tipo, identificacion, nombre, apellido, email, contrasena)
                self.mostrarDatos()
                self.limpiarCampos()
                messagebox.showinfo(title="Listo", message="Se ha registrado correctamente al Cliente")
                self.destroy()
            else:
                messagebox.showerror("Error, los campos no pueden estar vacios")
        except Exception as e:
            messagebox.showerror(message={e},title="Ha ocurrido un error:")










