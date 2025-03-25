#!/usr/bin/python
#*-------------------------------------------------------------------------*
#* factorial.py                                                            *
#* calcula el factorial de un número                                       *
#* Dr.P.E.Colla (c) 2022                                                   *
#* Creative commons                                                        *
#*-------------------------------------------------------------------------*
import sys 

def factorial(num): 
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

# Función para procesar la entrada y extraer los límites del rango
def obtener_rango(entrada):
    try:
        if entrada.startswith('-'):  # Caso "-hasta"
            desde = 1
            hasta = int(entrada[1:])
        elif entrada.endswith('-'):  # Caso "desde-"
            desde = int(entrada[:-1])
            hasta = 60
        else:  # Caso "desde-hasta"
            desde, hasta = map(int, entrada.split('-'))

        if desde > hasta:
            print("El primer número debe ser menor o igual al segundo.")
            sys.exit(1)

        return desde, hasta
    except ValueError:
        print("Formato incorrecto. Debe ser en el formato desde-hasta, -hasta o desde-.")
        sys.exit(1)

# Verifica si se ha proporcionado un argumento
if len(sys.argv) < 2:
    entrada = input("Ingrese un rango en formato desde-hasta, -hasta o desde- (ej. 4-8, -10, 5-): ")
else:
    entrada = sys.argv[1]

# Obtiene los valores del rango
desde, hasta = obtener_rango(entrada)

# Calcula y muestra los factoriales en el rango
for num in range(desde, hasta + 1):
    print(f"Factorial de {num} es {factorial(num)}")