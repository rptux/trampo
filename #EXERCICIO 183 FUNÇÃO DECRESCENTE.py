#EXERCICIO 183 FUNÇÃO DECRESCENTE
import matplotlib.pyplot as plt
import numpy as np

# Definir a função
def h(x):
    return -3 * x + 2

# Valores de x
x = np.linspace(-10, 10, 400)
y = h(x)

# Criar o gráfico
plt.plot(x, y, label='h(x) = -3x + 2')
plt.scatter([0, 1], [2, -1], color='red')  # Pontos
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)

# Configurar título e rótulos dos eixos
plt.title('Gráfico da Função Linear h(x) = -3x + 2')
plt.xlabel('x')
plt.ylabel('h(x)')
plt.legend()

# Mostrar o gráfico
plt.show()
