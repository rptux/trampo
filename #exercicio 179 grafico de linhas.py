#exercicio 179 grafico de linhas 
import matplotlib.pyplot as plt

# Dados do exercício 179
dias = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
temperaturas = [20, 22, 21, 23, 24, 22, 25, 23, 24, 26]

# Criar o gráfico de linhas
plt.plot(dias, temperaturas, marker='o', linestyle='-', color='blue')

# Configurar título e rótulos dos eixos
plt.title('Variação da Temperatura ao Longo dos Dias')
plt.xlabel('Dia')
plt.ylabel('Temperatura (°C)')

# Mostrar o gráfico de linhas
plt.show()
