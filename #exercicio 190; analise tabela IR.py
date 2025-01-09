#exercicio 190; analise tabela IR
import matplotlib.pyplot as plt
import numpy as np

# Definir a função do Imposto de Renda
def imposto_de_renda(x):
    if x <= 1903.98:
        return 0
    elif x <= 2826.65:
        return 0.075 * (x - 1903.98)
    elif x <= 3751.05:
        return 0.075 * (2826.65 - 1903.98) + 0.15 * (x - 2826.65)
    elif x <= 4664.68:
        return 0.075 * (2826.65 - 1903.98) + 0.15 * (3751.05 - 2826.65) + 0.225 * (x - 3751.05)
    else:
        return 0.075 * (2826.65 - 1903.98) + 0.15 * (3751.05 - 2826.65) + 0.225 * (4664.68 - 3751.05) + 0.275 * (x - 4664.68)

# Valores de x (salário mensal)
x = np.linspace(0, 7000, 500)
y = [imposto_de_renda(xi) for xi in x]

# Criar o gráfico
plt.plot(x, y, label='Imposto de Renda')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(color='gray', linestyle='--', linewidth=0.5)

# Configurar título e rótulos dos eixos
plt.title('Gráfico do Imposto de Renda')
plt.xlabel('Salário (R$)')
plt.ylabel('Imposto de Renda (R$)')
plt.legend()

# Mostrar o gráfico
plt.show()
