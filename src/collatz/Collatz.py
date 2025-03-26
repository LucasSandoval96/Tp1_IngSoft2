import matplotlib.pyplot as plt

def collatz_steps(n):
    """Calcula el número de pasos para que n llegue a 1 en la conjetura de Collatz."""
    steps = 0
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        steps += 1
    return steps

def plot_collatz():
    """Genera y muestra el gráfico de los pasos necesarios para que los números 1-10000 converjan."""
    numbers = list(range(1, 10001))
    iterations = [collatz_steps(n) for n in numbers]

    plt.figure(figsize=(10, 6))
    plt.scatter(iterations, numbers, s=1, color='blue', alpha=0.5)  # Gráfico de dispersión
    plt.xlabel("Número de iteraciones")
    plt.ylabel("Número inicial (n)")
    plt.title("Número de Collatz y cantidad de iteraciones hasta converger")
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    plot_collatz()
