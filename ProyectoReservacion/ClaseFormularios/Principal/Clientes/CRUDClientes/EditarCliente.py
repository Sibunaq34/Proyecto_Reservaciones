import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from ClasesNegocios.Usuarios import Usuarios

class EditarCliente(tk.Toplevel): 

    def __init__(self, master=None, email = None, contrasena = None):
        super().__init__(master)
        self.email= email
        self.contrasena = contrasena
        self.title("Editar Usuario")
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
        self.tabla.bind("<ButtonRelease-1>", self.seleccionarUsuarioTabla)

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
        
        self.btn_editar = tk.Button(self, text="Editar Usuario", command= self.editarUsuario, bg="#666a88", fg="#fcfcfc")
        self.btn_editar.grid(row=8, columnspan=2, sticky=("W"))
        self.mostrarDatos()

    def limpiarCampos(self):
        self.txt_id.delete(0, tk.END)
        self.txt_nombre.delete(0, tk.END)
        self.txt_apellido.delete(0, tk.END)
        self.txt_email.delete(0, tk.END)
        self.txt_contrasena.delete(0, tk.END)


    def mostrarDatos(self):

        xmlusuarios= ArchivoClientes()
        usuario = xmlusuarios.leerCliente(self.email, self.contrasena) #Envia esto para comprobar que es el mismo usuario y que no muestre otros datos

        if usuario:  #Comprueba que el email y contrasena esten con datos 
            self.tabla.insert("",tk.END, values=(
                usuario.get("Identificacion", ""),
                usuario.get("Nombre",""),
                usuario.get("Apellidos",""),
                usuario.get("Email", ""),
                usuario.get("Contrasena",""),
                usuario.get("Tipo", "")
            ))
    
    def seleccionarUsuarioTabla(self, event):
        item = self.tabla.focus()
        if item:
            valores = self.tabla.item(item, "values")
            self.txt_id.delete(0, tk.END)
            self.txt_id.insert(0, valores[0])
            self.txt_nombre.delete(0, tk.END)
            self.txt_nombre.insert(0, valores[1])
            self.txt_apellido.delete(0, tk.END)
            self.txt_apellido.insert(0, valores[2])
            self.txt_email.delete(0, tk.END)
            self.txt_email.insert(0, valores[3])
            self.txt_contrasena.delete(0, tk.END)
            self.txt_contrasena.insert(0, valores[4])


    
    def editarUsuario (self):
        if not self.txt_id.get():
            messagebox.showerror(title="Error", message="Debe de seleccionar un usuario")
            return
        
        tipo = "Cliente"
        usuario =  Usuarios(int(self.txt_id.get()),self.txt_nombre.get(),self.txt_apellido.get(),self.txt_email.get(),self.txt_contrasena.get(), tipo)

        xmlclientes = ArchivoClientes()

        if xmlclientes.modificarXml(usuario):
            messagebox.showinfo(title="Listo", message="Se ha editado correctamente al cliente")
            self.mostrarDatos()
            self.limpiarCampos()
            self.destroy()
        else:
            messagebox.showerror(title="Error", message="No se ha podido editar el cliente")










