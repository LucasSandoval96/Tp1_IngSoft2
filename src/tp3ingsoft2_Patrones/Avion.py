class Avion:
    def __init__(self):
        self.partes = []

    def mostrar(self):
        print("Partes del avión:", ", ".join(self.partes))

class AvionBuilder:
    def __init__(self):
        self.avion = Avion()

    def construir_body(self):
        self.avion.partes.append("Body")

    def construir_turbinas(self):
        self.avion.partes.append("Turbina 1")
        self.avion.partes.append("Turbina 2")

    def construir_alas(self):
        self.avion.partes.append("Ala izquierda")
        self.avion.partes.append("Ala derecha")

    def construir_tren_aterrizaje(self):
        self.avion.partes.append("Tren de aterrizaje")

    def obtener_avion(self):
        return self.avion
