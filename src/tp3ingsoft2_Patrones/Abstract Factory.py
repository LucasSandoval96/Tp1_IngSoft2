# Interfaz abstracta
class GUIFactory:
    def crear_boton(self): pass
    def crear_menu(self): pass

# Implementaciones concretas
class WindowsFactory(GUIFactory):
    def crear_boton(self):
        return "Botón estilo Windows"
    def crear_menu(self):
        return "Menú estilo Windows"

class LinuxFactory(GUIFactory):
    def crear_boton(self):
        return "Botón estilo Linux"
    def crear_menu(self):
        return "Menú estilo Linux"
