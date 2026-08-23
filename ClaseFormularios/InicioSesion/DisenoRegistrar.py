import tkinter as tk
from tkinter import ttk
from tkinter.font import BOLD
from tkinter import messagebox
from ClasesDatos.Clientes import *
from ClasesDatos.Dueno  import *
from ClasesNegocios.Usuarios import Usuarios

class FormularioRegistrar: 

    def __init__(self):
        self.seleccion = tk.StringVar()
        self.ventana = tk.Tk()
        self.ventana.title ("Registrarse")
        self.ventana.geometry("800x800")
        self.ventana.config(bg="#fcfcfc")
        self.ventana.resizable(width=0, height=0)

        ##Marco para logo 

        frame_logo = tk.Frame(self.ventana, bd=0, width=300, relief=tk.SOLID, padx=10, pady=10, bg="#bb4141")
        frame_logo.pack(side="left", expand=tk.NO, fill=tk.BOTH)

        #Marco para el formulario de inicio de sesion
        frame_principal = tk.Frame(self.ventana, bd = 0, relief=tk.SOLID, bg="#fcfcfc")
        frame_principal.pack(side="right", expand=tk.YES, fill=tk.BOTH)

        #Marco para el titulo
        frame_registrarse = tk.Frame(frame_principal, height= 50, bd=0, relief=tk.SOLID, bg="black")
        frame_registrarse.pack(side="top",fill=tk.X)
        lbl_registrarse = tk.Label(frame_registrarse, text="Registrarse", font=("Time", 30), fg="#666a88",bg="#fcfcfc", pady=50)
        lbl_registrarse.pack(expand=tk.YES,fill=tk.BOTH)

        #Marco para el boton

        frame_formulario = tk.Frame(frame_principal,height = 50, bd=0, relief=tk.SOLID,bg="#fcfcfc")
        frame_formulario.pack(side="bottom", expand=tk.YES, fill=tk.BOTH)
       

        lbl_identificacion = tk.Label(frame_formulario, text="Identificacion", font=("Time", 14), fg="#666a88",bg="#fcfcfc", anchor="w")
        lbl_identificacion.pack(fill=tk.X, padx=20, pady=5)
        self.txt_identificacion = tk.Entry(frame_formulario, font=("Times", 14))
        self.txt_identificacion.pack(fill=tk.X, padx=20, pady=10)


        lbl_nombre = tk.Label(frame_formulario, text="Nombre", font=("Time", 14), fg="#666a88",bg="#fcfcfc", anchor="w")
        lbl_nombre.pack(fill=tk.X, padx=20, pady=5)
        self.txt_nombre = tk.Entry(frame_formulario, font=("Times", 14))
        self.txt_nombre.pack(fill=tk.X, padx=20, pady=10)


        lbl_apellidos = tk.Label(frame_formulario, text="Apellidos", font=("Time", 14), fg="#666a88",bg="#fcfcfc", anchor="w")
        lbl_apellidos.pack(fill=tk.X, padx=20, pady=5)
        self.txt_apellidos= tk.Entry(frame_formulario, font=("Times", 14))
        self.txt_apellidos.pack(fill=tk.X, padx=20, pady=10)

        lbl_email = tk.Label(frame_formulario, text="Email", font=("Time", 14), fg="#666a88",bg="#fcfcfc", anchor="w")
        lbl_email.pack(fill=tk.X, padx=20, pady=5)
        self.txt_email = tk.Entry(frame_formulario, font=("Times", 14))
        self.txt_email.pack(fill=tk.X, padx=20, pady=10)


        lbl_contrasena = tk.Label(frame_formulario, text="Contraseña", font=("Times", 14), fg="#666a88", bg="#fcfcfc", anchor="w")
        lbl_contrasena.pack(fill=tk.X, padx=20, pady=5)
        self.txt_contrasena = tk.Entry(frame_formulario, font=("Times", 14))
        self.txt_contrasena.pack(fill=tk.X, padx=20, pady=10)
        self.txt_contrasena.config(show="*")

        lbl_tipo = tk.Label(frame_formulario, text="Tipo de cuenta:", font=("Time", 14), fg="#666a88",bg="#fcfcfc", anchor="w")
        lbl_tipo.pack(fill=tk.X, padx=20, pady=5)

        self.cbx_tipo = ttk.Combobox(frame_formulario, textvariable=self.seleccion)
        self.cbx_tipo['values'] = ["Cliente", "Dueno"]
        self.cbx_tipo.pack(fill=tk.X, padx=20, pady=5)

        btn_registrarse= tk.Button(frame_formulario, text="Registrarse", font=("Times", 15, BOLD), bg="#3a7ff6", bd=0, fg="#fff", command=self.registrar)
        btn_registrarse.pack(fill=tk.X, padx=20, pady=20)
        btn_registrarse.bind("<Return>", (lambda event: self.registrar()))
        self.ventana.mainloop()

    def registrar(self):
        xmlclientes = ArchivoClientes()
        xmlduenos = ArchivoDuenos()
        try:
            
            if self.txt_identificacion.get() and self.txt_nombre.get() and self.txt_apellidos.get() and self.txt_email.get() and self.txt_contrasena.get():
                identificacion = int(self.txt_identificacion.get())
                nombre = self.txt_nombre.get()
                apellido = self.txt_apellidos.get()
                email = self.txt_email.get()
                contrasena = self.txt_contrasena.get()
                tipo = self.cbx_tipo.get()

                if tipo == "Cliente":
                    cliente = xmlclientes.validarRegisrtro(identificacion,email)
                    if cliente:
                        messagebox.showerror(title="Error", message="Ya existe una con la identificacion o con el email")
                        return
                    clientes = Usuarios(identificacion, nombre, apellido, email, contrasena, tipo)

                    xmlclientes.escribirXml(clientes)
                    messagebox.showinfo(title="Listo", message="Se ha registrado correctamente al Cliente")
                    self.ventana.destroy()
                else:
                    dueno= xmlduenos.validacionRegistro(identificacion, email)
                    if dueno:
                        messagebox.showerror(title="Error", message="La identidifacion y correo electronico ya fueron registrados")
                        return
                    duenos = Usuarios(identificacion, nombre, apellido, email, contrasena, tipo)

                    xmlduenos.escribirXml(duenos)
                    messagebox.showinfo(title="Listo", message="Se ha registrado correctamente al Dueños")
                    self.ventana.destroy()

            else:
                messagebox.showerror("Error, los campos no pueden estar vacios")
        except Exception as e:
            messagebox.showerror(message={e},title="Ha ocurrido un error:")

