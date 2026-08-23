import os
from ClaseFormularios.InicioSesion.Logica import *

def borrarPantalla(): 
    if os.name == "posix":
        os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system ("cls")

if __name__ == "__main__":
    InicioSesion()
    #main()