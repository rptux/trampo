#EXERCICIO 184 FUNÇÃO 2 GRAU
import matplotlib.pyplot as plt
import numpy as np

# Definir a função
def f(x):
    return x**2 - 4 * x + 3

# Valores de x
x = np.linspace(-2, 6, 400)
y = f(x)

# Criar o gráfico
plt.plot(x, y, label='f(x) = x^2 - 4x + 3')
plt.scatter([0, 1, 2, 3, 4], [3, 0, -1, 0, 3], color='red')  # Pontos
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(color='gray', linestyle='--', linewidth=0.5)

# Configurar título e rótulos dos eixos
plt.title('Gráfico da Função Quadrática f(x) = x^2 - 4x + 3')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()

# Mostrar o gráfico
plt.show()
