#EXERCICIO 185
import matplotlib.pyplot as plt
import numpy as np

# Definir a função
def g(x):
    return 2 * x**2

# Valores de x
x = np.linspace(-3, 3, 400)
y = g(x)

# Criar o gráfico
plt.plot(x, y, label='g(x) = 2x^2')
plt.scatter([0, 1, 2, -1, -2], [0, 2, 8, 2, 8], color='red')  # Pontos
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(color='gray', linestyle='--', linewidth=0.5)

# Configurar título e rótulos dos eixos
plt.title('Gráfico da Função Quadrática g(x) = 2x^2')
plt.xlabel('x')
plt.ylabel('g(x)')
plt.legend()

# Mostrar o gráfico
plt.show()
