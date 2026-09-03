import tkinter as tk
from tkinter import ttk
from tkinter.font import BOLD

class FormularioInicioSesion: 

    def __init__(self):

        self.ventana = tk.Tk()
        self.ventana.title ("Inicio de sesion")
        self.ventana.geometry("800x600")
        self.ventana.config(bg="#fcfcfc")
        self.ventana.resizable(width=0, height=0)

        ##Marco para logo 

        frame_logo = tk.Frame(self.ventana, bd=0, width=300, relief=tk.SOLID, padx=10, pady=10, bg="#4198bb")
        frame_logo.pack(side="left", expand=tk.NO, fill=tk.BOTH)

        #Marco para el formulario de inicio de sesion
        frame_principal = tk.Frame(self.ventana, bd = 0, relief=tk.SOLID, bg="#fcfcfc")
        frame_principal.pack(side="right", expand=tk.YES, fill=tk.BOTH)

        #Marco para el titulo
        frame_ini_sesion = tk.Frame(frame_principal, height= 50, bd=0, relief=tk.SOLID, bg="black")
        frame_ini_sesion.pack(side="top",fill=tk.X)
        lbl_ini_sesion = tk.Label(frame_ini_sesion, text="Inicio de sesion", font=("Time", 30), fg="#666a88",bg="#fcfcfc", pady=50)
        lbl_ini_sesion.pack(expand=tk.YES,fill=tk.BOTH)

        #Marco para el boton

        frame_boton = tk.Frame(frame_principal,height = 50, bd=0, relief=tk.SOLID,bg="#fcfcfc")
        frame_boton.pack(side="bottom", expand=tk.YES, fill=tk.BOTH)
       
        lbl_usuario = tk.Label(frame_boton, text="Usuario", font=("Time", 14), fg="#666a88",bg="#fcfcfc", anchor="w")
        lbl_usuario.pack(fill=tk.X, padx=20, pady=5)
        self.usuario = tk.Entry(frame_boton, font=("Times", 14))
        self.usuario.pack(fill=tk.X, padx=20, pady=10)

        lbl_contrasena = tk.Label(frame_boton, text="Contraseña", font=("Times", 14), fg="#666a88", bg="#fcfcfc", anchor="w")
        lbl_contrasena.pack(fill=tk.X, padx=20, pady=5)
        self.contrasena = tk.Entry(frame_boton, font=("Times", 14))
        self.contrasena.pack(fill=tk.X, padx=20, pady=10)
        self.contrasena.config(show="*")

        btn_ini_sesion= tk.Button(frame_boton, text="Iniciar Sesion", font=("Times", 15, BOLD), bg="#3a7ff6", bd=0, fg="#fff", command=self.validacion)
        btn_ini_sesion.pack(fill=tk.X, padx=20, pady=20)
        btn_ini_sesion.bind("<Return>", (lambda event: self.validacion()))

        btn_registrar= tk.Button(frame_boton, text="Registrar", font=("Times", 15, BOLD), bg="#fcfcfc", bd=0, fg="#3a7ff6", command=self.registro)
        btn_registrar.pack(fill=tk.X, padx=20, pady=20)
        btn_registrar.bind("<Return>", (lambda event: self.registro()))
        self.ventana.mainloop()


