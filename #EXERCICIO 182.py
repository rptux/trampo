#EXERCICIO 182
import matplotlib.pyplot as plt
import numpy as np

# Definir a função
def g(x):
    return 4 * x

# Valores de x
x = np.linspace(-10, 10, 400)
y = g(x)

# Criar o gráfico
plt.plot(x, y, label='g(x) = 4x')
plt.scatter([0, 1], [0, 4], color='red')  # Pontos
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)

# Configurar título e rótulos dos eixos
plt.title('Gráfico da Função Linear g(x) = 4x')
plt.xlabel('x')
plt.ylabel('g(x)')
plt.legend()

# Mostrar o gráfico
plt.show()
