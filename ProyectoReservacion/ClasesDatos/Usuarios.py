import xml.etree.ElementTree as ET
import os


class ArchivosUsuarios:

    def __init__(self):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        self.ruta = os.path.join(base_dir, '../ClasesDatos/Archivos/Usuarios.xml')
        # Crear carpeta si no existe
        carpeta = os.path.dirname(self.ruta)
        if not os.path.exists(carpeta):
            os.makedirs(carpeta)
            
        if not os.path.exists(self.ruta):
            root = ET.Element("usuarios")  # Raíz del XML
            tree = ET.ElementTree(root)
            tree.write(self.ruta, encoding="utf-8", xml_declaration=True)

    #region CRUD para administador

    def escribir_xml(self, tipo,identificacion,nombre, apellido,email, contrasena ):
            # Cargar el XML si es válido, sino crear uno nuevo
            if os.path.exists(self.ruta) and os.path.getsize(self.ruta) > 0:
                try:
                    tree = ET.parse(self.ruta)
                    raiz = tree.getroot()
                except ET.ParseError:
                    print("XML corrupto, se reiniciará.")
                    raiz = ET.Element("usuarios")
                    tree = ET.ElementTree(raiz)
            else:
                raiz = ET.Element("usuarios")
                tree = ET.ElementTree(raiz)

            cliente = ET.Element(tipo)
            ET.SubElement(cliente, "Identificacion").text = str(identificacion)
            ET.SubElement(cliente, "Nombre").text = nombre
            ET.SubElement(cliente, "Apellidos").text = apellido
            ET.SubElement(cliente, "Email").text = email
            ET.SubElement(cliente, "Contrasena").text = contrasena

            raiz.append(cliente)
            tree.write(self.ruta, encoding="utf-8", xml_declaration=True)
            

    def leer_xml(self):
        usuarios = []

        if os.path.exists(self.ruta) and os.path.getsize(self.ruta) > 0:
            tree = ET.parse(self.ruta)
            raiz = tree.getroot()

            for nodos in raiz:
                if nodos.tag in ("Cliente", "Dueno"):

                    usuarios.append({
                        "Identificacion": nodos.findtext("Identificacion", ""),
                        "Nombre": nodos.findtext("Nombre", ""),
                        "Apellidos": nodos.findtext("Apellidos", ""),
                        "Email": nodos.findtext("Email", ""),
                        "Contrasena": nodos.findtext("Contrasena", ""),
                    })

        return usuarios

    def filtrar_usuarios(self, tipo, identificacion):
        usuarios = []

        if os.path.exists(self.ruta) and os.path.getsize(self.ruta) > 0:
            tree = ET.parse(self.ruta)
            raiz = tree.getroot()

            for nodos in raiz.findall(tipo):
                if identificacion in nodos.findtext("Identificacion", ""):
                    usuarios.append({
                        "Identificacion": nodos.findtext("Identificacion", ""),
                        "Nombre": nodos.findtext("Nombre", ""),
                        "Apellidos": nodos.findtext("Apellidos", ""),
                        "Email": nodos.findtext("Email", ""),
                        "Contrasena": nodos.findtext("Contrasena", ""),
                    })

        return usuarios


    def leer_clientes(self):
        usuarios = []

        if os.path.exists(self.ruta) and os.path.getsize(self.ruta) > 0:
            tree = ET.parse(self.ruta)
            raiz = tree.getroot()

            for nodos in raiz.findall("Cliente"):
                usuarios.append({
                    "Identificacion": nodos.findtext("Identificacion", ""),
                    "Nombre": nodos.findtext("Nombre", ""),
                    "Apellidos": nodos.findtext("Apellidos", ""),
                    "Email": nodos.findtext("Email", ""),
                    "Contrasena": nodos.findtext("Contrasena", ""),
                })

        return usuarios


    def leer_duenos(self):
        usuarios = []

        if os.path.exists(self.ruta) and os.path.getsize(self.ruta) > 0:
            tree = ET.parse(self.ruta)
            raiz = tree.getroot()

            for nodos in raiz.findall("Dueno"):
                usuarios.append({
                    "Identificacion": nodos.findtext("Identificacion", ""),
                    "Nombre": nodos.findtext("Nombre", ""),
                    "Apellidos": nodos.findtext("Apellidos", ""),
                    "Email": nodos.findtext("Email", ""),
                    "Contrasena": nodos.findtext("Contrasena", ""),
                })

        return usuarios


    def modificar_xml(self,tipo, identificacion, nombre, apellido, email, contrasena):
        if not os.path.exists(self.ruta):
             return False
        tree = ET.parse(self.ruta)
        raiz = tree.getroot()
        actualizado = False

        for nodo in raiz.findall(tipo):
            if nodo.find("Identificacion").text == str(identificacion):
                 nodo.find("Nombre").text = nombre
                 nodo.find("Apellidos").text =apellido
                 nodo.find("Email").text =email
                 nodo.find("Contrasena").text =contrasena
                 actualizado = True
                 break
        
        if actualizado: 
            tree.write(self.ruta, encoding="utf-8", xml_declaration=True)

        return actualizado
    

    def eliminar_usuario(self, tipo, identificacion):

        if not os.path.exists(self.ruta):
            return False
        
        tree = ET.parse(self.ruta)
        raiz = tree.getroot()
        eliminado = False

        for nodo in raiz.findall(tipo):
            if nodo.find("Identificacion").text == str(identificacion):
                raiz.remove(nodo)
                eliminado = True
                break
        
        if eliminado:
            tree.write(self.ruta, encoding="utf-8", xml_declaration=True)
        return eliminado
    

    #endregion  


    def inicio_sesion(self,tipo, email, contrasena):

        if tipo == "Cliente":
            clientes = self.leer_clientes()
            for cliente in clientes:
                if cliente["Email"] == email and cliente["Contrasena"] == contrasena:
                    return cliente
        if tipo == "Dueno":
            duenos = self.leer_duenos()
            for dueno in duenos:
                if dueno["Email"] == email and dueno["Contrasena"] == contrasena:
                    return dueno

        return None


    def validar_regisrtro(self, tipo, identificacion, email):
        clientes = self.leer_clientes()
        duenos = self.leer_duenos()
        if tipo == "Cliente":
            for cliente in clientes:
                if cliente["Identificacion"] == str(identificacion) or cliente["Email"] == email:
                    return cliente
        elif tipo == "Dueno":
            for dueno in duenos:
                if dueno["Identificacion"] == str(identificacion) or dueno["Email"] == email:
                    return dueno
        return None
    

    def buscar_usuario(self,tipo, email):
        clientes = self.leer_clientes()
        duenos = self.leer_duenos()

        if tipo == "Cliente":
            for cliente in clientes:
                if cliente["Email"]== email:
                    return cliente["Identificacion"]
        elif tipo == "Dueno":
            for dueno in duenos:
                if dueno["Email"] == email:
                    return dueno["Identificacion"]
        
        return None

    


             







