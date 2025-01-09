#variação de temperatura
import matplotlib.pyplot as plt
import numpy as np

# Dados fictícios da temperatura ao longo de um dia (em °C)
horas = np.arange(0, 24)
temperaturas = [16, 15, 14, 13, 12, 13, 15, 18, 21, 24, 26, 28, 30, 31, 30, 28, 26, 24, 22, 21, 20, 19, 18, 17]

# Criar o gráfico
plt.figure(figsize=(12, 6))
plt.plot(horas, temperaturas, marker='o', linestyle='-', color='r')

# Adicionar título e rótulos aos eixos
plt.title('Variação da Temperatura ao Longo do Dia')
plt.xlabel('Hora do Dia')
plt.ylabel('Temperatura (°C)')

# Adicionar grade
plt.grid(True)

# Mostrar o gráfico
plt.show()
