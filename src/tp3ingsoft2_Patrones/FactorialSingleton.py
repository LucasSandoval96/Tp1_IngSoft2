class FactorialSingleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(FactorialSingleton, cls).__new__(cls)
        return cls._instance

    def calcular(self, n):
        if n < 0:
            raise ValueError("No se puede calcular el factorial de un número negativo.")
        resultado = 1
        for i in range(2, n + 1):
            resultado *= i
        return resultado
