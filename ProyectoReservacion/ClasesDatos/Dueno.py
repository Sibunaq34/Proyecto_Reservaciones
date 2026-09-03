import xml.etree.ElementTree as ET
from ClasesNegocios import Usuarios
import os

class ArchivoDuenos: 

    def __init__(self):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        self.ruta = os.path.join(base_dir, '../ClasesDatos/Datos/Duenos.xml')
        # Crear carpeta si no existe
        carpeta = os.path.dirname(self.ruta)
        if not os.path.exists(carpeta):
            os.makedirs(carpeta)
            
        if not os.path.exists(self.ruta):
            root = ET.Element("Duenos")  # Raíz del XML
            tree = ET.ElementTree(root)
            tree.write(self.ruta, encoding="utf-8", xml_declaration=True)
#region CRUD
    
    def escribirXml(self, usuario: Usuarios):
            # Cargar el XML si es válido, sino crear uno nuevo
            if os.path.exists(self.ruta) and os.path.getsize(self.ruta) > 0:
                try:
                    tree = ET.parse(self.ruta)
                    raiz = tree.getroot()
                except ET.ParseError:
                    print("XML corrupto, se reiniciará.")
                    raiz = ET.Element("Duenos")
                    tree = ET.ElementTree(raiz)
            else:
                raiz = ET.Element("Duenos")
                tree = ET.ElementTree(raiz)

            dueno = ET.Element("Dueno")
            ET.SubElement(dueno, "Identificacion").text = str(usuario.Identificacion)
            ET.SubElement(dueno, "Nombre").text = usuario.Nombre
            ET.SubElement(dueno, "Apellidos").text = usuario.Apellido
            ET.SubElement(dueno, "Email").text = usuario.Email
            ET.SubElement(dueno, "Contrasena").text = usuario.Contrasena
            ET.SubElement(dueno, "Tipo").text = usuario.Tipo

            raiz.append(dueno)
            tree.write(self.ruta, encoding="utf-8", xml_declaration=True)
    

    def leerXml(self):
        duenos = []

        if os.path.exists(self.ruta) and os.path.getsize(self.ruta) > 0:
            tree = ET.parse(self.ruta)
            raiz = tree.getroot()

            for nodos in raiz.findall("Dueno"):
                duenos.append({
                    "Identificacion": nodos.findtext("Identificacion", ""),
                    "Nombre": nodos.findtext("Nombre", ""),
                    "Apellidos": nodos.findtext("Apellidos", ""),
                    "Email": nodos.findtext("Email", ""),
                    "Contrasena": nodos.findtext("Contrasena", ""),
                    "Tipo": nodos.findtext("Tipo", "")

                })
        
        return duenos
    

    def modificarXml(self, usuario:Usuarios):
        if not os.path.exists(self.ruta):
             return False
        tree = ET.parse(self.ruta)
        raiz = tree.getroot()
        actualizado = False

        for nodo in raiz.findall("Dueno"):
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
    

    def eliminarDueno(self, usuario: Usuarios):

        if not os.path.exists(self.ruta):
            return False
        
        tree = ET.parse(self.ruta)
        raiz = tree.getroot()
        eliminado = False

        for nodo in raiz.findall("Dueno"):
            if nodo.find("Identificacion").text == str(usuario.Identificacion):
                raiz.remove(nodo)
                eliminado = True
                break
        
        if eliminado:
            tree.write(self.ruta, encoding="utf-8", xml_declaration=True)
        return eliminado

 #endregion
          
    def inicioSesion(self, email, contrasena):
        duenos = self.leerXml()

        for dueno in duenos:
            if dueno["Email"] == email and dueno["Contrasena"] == contrasena:
                return dueno
        
        return None
    
    def validacionRegistro(self, identificacion, email):
        duenos = self.leerXml()

        for dueno in duenos:
            if dueno["Identificacion"]== str(identificacion) or  dueno["Email"]==email:
                return dueno
        
        return None
    
    def validacionDueno(self, identificacion):
        duenos = self.leerXml()

        for dueno in duenos:
            if dueno["Identificacion"]== str(identificacion):
                return dueno
        
        return None
    
    



