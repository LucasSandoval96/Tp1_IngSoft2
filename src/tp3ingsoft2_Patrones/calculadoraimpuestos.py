class CalculadoraImpuestos:
    def calcular_total(self, base):
        iva = base * 0.21
        iibb = base * 0.05
        contribuciones = base * 0.012
        return base + iva + iibb + contribuciones
