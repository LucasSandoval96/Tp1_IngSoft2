import copy

class Prototipo:
    def clonar(self):
        return copy.deepcopy(self)

class ClaseDerivada(Prototipo):
    def __init__(self, dato):
        self.dato = dato

