#EXERCICIO 186
import matplotlib.pyplot as plt
import numpy as np

# Definir a função
def h(x):
    return x**2 + 2 * x + 1

# Valores de x
x = np.linspace(-3, 3, 400)
y = h(x)

# Criar o gráfico
plt.plot(x, y, label='h(x) = x^2 + 2x + 1')
plt.scatter([0, 1, -1, 2, -2], [1, 4, 0, 9, 1], color='red')  # Pontos
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(color='gray', linestyle='--', linewidth=0.5)

# Configurar título e rótulos dos eixos
plt.title('Gráfico da Função Quadrática h(x) = x^2 + 2x + 1')
plt.xlabel('x')
plt.ylabel('h(x)')
plt.legend()

# Mostrar o gráfico
plt.show()
