class Factura:
    def __init__(self, importe, condicion):
        self.importe = importe
        self.condicion = condicion

    def imprimir(self):
        print(f"Factura: ${self.importe:.2f} - Condición impositiva: {self.condicion}")
