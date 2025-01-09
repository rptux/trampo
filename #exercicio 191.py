#exercicio 191
import matplotlib.pyplot as plt
import numpy as np

# Definir a função da conta de energia elétrica
def conta_energia(x):
    if x <= 100:
        return 0.50 * x
    elif x <= 200:
        return 0.50 * 100 + 0.75 * (x - 100)
    else:
        return 0.50 * 100 + 0.75 * 100 + 1.00 * (x - 200)

# Valores de x (consumo mensal em kWh)
x = np.linspace(0, 300, 500)
y = [conta_energia(xi) for xi in x]

# Criar o gráfico
plt.plot(x, y, label='Conta de Energia Elétrica')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(color='gray', linestyle='--', linewidth=0.5)

# Configurar título e rótulos dos eixos
plt.title('Gráfico da Conta de Energia Elétrica')
plt.xlabel('Consumo (kWh)')
plt.ylabel('Custo (R$)')
plt.legend()

# Mostrar o gráfico
plt.show()
