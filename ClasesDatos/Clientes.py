import xml.etree.ElementTree as ET
from ClasesNegocios.Usuarios import Usuarios
import os

class ArchivoClientes: 

    def __init__(self):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        self.ruta = os.path.join(base_dir, '../ClasesDatos/Datos/Clientes.xml')
        # Crear carpeta si no existe
        carpeta = os.path.dirname(self.ruta)
        if not os.path.exists(carpeta):
            os.makedirs(carpeta)
            
        if not os.path.exists(self.ruta):
            root = ET.Element("Clientes")  # Raíz del XML
            tree = ET.ElementTree(root)
            tree.write(self.ruta, encoding="utf-8", xml_declaration=True)

    #region CRUD para administador

    def escribirXml(self, usuario: Usuarios):
            # Cargar el XML si es válido, sino crear uno nuevo
            if os.path.exists(self.ruta) and os.path.getsize(self.ruta) > 0:
                try:
                    tree = ET.parse(self.ruta)
                    raiz = tree.getroot()
                except ET.ParseError:
                    print("XML corrupto, se reiniciará.")
                    raiz = ET.Element("Clientes")
                    tree = ET.ElementTree(raiz)
            else:
                raiz = ET.Element("Clientes")
                tree = ET.ElementTree(raiz)

            cliente = ET.Element("Cliente")
            ET.SubElement(cliente, "Identificacion").text = str(usuario.Identificacion)
            ET.SubElement(cliente, "Nombre").text = usuario.Nombre
            ET.SubElement(cliente, "Apellidos").text = usuario.Apellido
            ET.SubElement(cliente, "Email").text = usuario.Email
            ET.SubElement(cliente, "Contrasena").text = usuario.Contrasena
            ET.SubElement(cliente, "Tipo").text = usuario.Tipo

            raiz.append(cliente)
            tree.write(self.ruta, encoding="utf-8", xml_declaration=True)
            
    
    def leerXml(self):
        clientes = []

        if os.path.exists(self.ruta) and os.path.getsize(self.ruta) > 0:
            tree = ET.parse(self.ruta)
            raiz = tree.getroot()

            for nodos in raiz.findall("Cliente"):
                clientes.append({
                    "Identificacion": nodos.findtext("Identificacion", ""),
                    "Nombre": nodos.findtext("Nombre", ""),
                    "Apellidos": nodos.findtext("Apellidos", ""),
                    "Email": nodos.findtext("Email", ""),
                    "Contrasena": nodos.findtext("Contrasena", ""),
                    "Tipo": nodos.findtext("Tipo", "")

                })
        
        return clientes
    

    def modificarXml(self, usuario:Usuarios):
        if not os.path.exists(self.ruta):
             return False
        tree = ET.parse(self.ruta)
        raiz = tree.getroot()
        actualizado = False

        for nodo in raiz.findall("Cliente"):
            if nodo.find("Identificacion").text == str(usuario.Identificacion):
                 nodo.find("Nombre").text = usuario.Nombre
                 nodo.find("Apellidos").text =usuario.Apellido
                 nodo.find("Email").text = usuario.Email
                 nodo.find("Contrasena").text = usuario.Contrasena
                 nodo.find("Tipo").text = usuario.Tipo

                 actualizado = True
                 break
        
        if actualizado: 
            tree.write(self.ruta, encoding="utf-8", xml_declaration=True)

        return actualizado
    

    def eliminarCliente(self, usuario: Usuarios):

        if not os.path.exists(self.ruta):
            return False
        
        tree = ET.parse(self.ruta)
        raiz = tree.getroot()
        eliminado = False

        for nodo in raiz.findall("Cliente"):
            if nodo.find("Identificacion").text == str(usuario.Identificacion):
                raiz.remove(nodo)
                eliminado = True
                break
        
        if eliminado:
            tree.write(self.ruta, encoding="utf-8", xml_declaration=True)
        return eliminado
    

    #endregion  


    def inicioSesion(self, email, contrasena):
        clientes = self.leerXml()

        for cliente in clientes:
            if cliente["Email"] == email and cliente["Contrasena"] == contrasena:
                return cliente
        
        return None
    
    def validarRegisrtro(self, identificacion, email):
        clientes = self.leerXml()

        for cliente in clientes:
            if cliente["Identificacion"] == str(identificacion) or cliente["Email"] == email:
                return cliente
        
        return None
    

    def validacionCliente(self, identificacion):
        clientes = self.leerXml()

        for cliente in clientes:
            if cliente["Identificacion"]== str(identificacion):
                return cliente
        
        return None


    def leerCliente(self, email, contrasena ):

        clientes = self.leerXml()

        for cliente in clientes:
            if cliente["Email"] == email and cliente["Contrasena"] == contrasena:
                return cliente
        
        return None
    


             







