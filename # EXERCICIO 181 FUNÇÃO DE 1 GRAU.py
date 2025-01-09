# EXERCICIO 181 FUNÇÃO DE 1 GRAU
import matplotlib.pyplot as plt
import numpy as np

# Definir a função
def f(x):
    return 2 * x + 3

# Valores de x
x = np.linspace(-10, 10, 400)
y = f(x)

# Criar o gráfico
plt.plot(x, y, label='f(x) = 2x + 3')
plt.scatter([0, 1], [3, 5], color='red')  # Pontos
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)

# Configurar título e rótulos dos eixos
plt.title('Gráfico da Função Linear f(x) = 2x + 3')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()

# Mostrar o gráfico
plt.show()
