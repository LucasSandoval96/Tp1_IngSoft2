#!/usr/bin/python
#*-------------------------------------------------------------------------*
#* factorial.py                                                            *
#* calcula el factorial de un número                                       *
#* Dr.P.E.Colla (c) 2022                                                   *
#* Creative commons                                                        *
#*-------------------------------------------------------------------------*
import sys

class Factorial:
    def __init__(self):
        pass  # No necesitamos inicializar atributos en este caso

    def calcular(self, num):
        if num < 0:
            return "Factorial de un número negativo no existe"
        elif num == 0:
            return 1
        else:
            fact = 1
            while num > 1:
                fact *= num
                num -= 1
            return fact

    def run(self, min, max):
        if min > max:
            print("El primer número debe ser menor o igual al segundo.")
            return
        for num in range(min, max + 1):
            print(f"Factorial de {num} es {self.calcular(num)}")

# Verificación de argumentos
if len(sys.argv) < 2:
    print("Debe informar un número o un rango!")
    entrada = input("Ingrese un número o rango (ej. 5 o 3-7): ")
else:
    entrada = sys.argv[1]

# Procesamiento de entrada
try:
    if '-' in entrada:  # Si es un rango "min-max"
        min_val, max_val = map(int, entrada.split('-'))
    else:  # Si es un único número
        min_val = max_val = int(entrada)

    # Creación de la instancia y ejecución
    factorial = Factorial()
    factorial.run(min_val, max_val)

except ValueError:
    print("Entrada no válida. Use un número o un rango en formato min-max.")


