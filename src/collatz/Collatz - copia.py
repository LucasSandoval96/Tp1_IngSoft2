import matplotlib.pyplot as plt

def collatz(n):
    """Calcula la secuencia de Collatz para un número dado.

    Args:
        n: El número entero para el que se calcula la secuencia.

    Returns:
        Una lista que contiene la secuencia de Collatz.
    """
    secuencia = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        secuencia.append(n)
    return secuencia

def calcular_iteraciones(n):
    """Calcula el número de iteraciones para que la secuencia de Collatz converja a 1.

    Args:
        n: El número entero para el que se calcula el número de iteraciones.

    Returns:
        El número de iteraciones necesarias para que la secuencia converja a 1.
    """
    secuencia = collatz(n)
    return len(secuencia) - 1

# Calcular los números de Collatz y las iteraciones para números del 1 al 10000
numeros = range(1, 10001)
iteraciones = [calcular_iteraciones(n) for n in numeros]

# Crear el gráfico
plt.figure(figsize=(10, 6))
plt.plot(numeros, iteraciones, 'bo-', markersize=2)
plt.xlabel('Número de inicio (n)')
plt.ylabel('Número de iteraciones')
plt.title('Conjetura de Collatz: Número de iteraciones para n = 1 a 10000')
plt.grid(True)
plt.show()

# Guardar el gráfico en un archivo
plt.savefig('src/collatz_graph.png')
