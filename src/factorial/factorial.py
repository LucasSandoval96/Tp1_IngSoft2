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
        print("Factorial de un número negativo no existe")
        return 0
    elif num == 0: 
        return 1
        
    else: 
        fact = 1
        while(num > 1): 
            fact *= num 
            num -= 1
        return fact 

def obtener_rango(entrada): # Función para procesar la entrada y extraer los límites del rango
    try:
        desde, hasta = map(int, entrada.split('-'))
        if desde > hasta:
            print("El primer número debe ser menor o igual al segundo.")
            sys.exit(1)
        return desde, hasta
    except ValueError:
        print("Formato incorrecto. Debe ser en el formato desde-hasta (ej. 4-8).")
        sys.exit(1)

if len(sys.argv) < 2:
    entrada = input("Ingrese un rango en formato desde-hasta (ej. 4-8): ")
else:
    entrada = sys.argv[1]

# Obtiene los valores del rango
desde, hasta = obtener_rango(entrada)

# Calcula y muestra los factoriales en el rango
for num in range(desde, hasta + 1):
    print(f"Factorial de {num} es {factorial(num)}")

#soy un comentario para la consigna