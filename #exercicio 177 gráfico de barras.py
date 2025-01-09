#exercicio 177 gráfico de barras
import matplotlib.pyplot as plt

# Dados do exercício 177
dias = ['1', '2', '3', '4', '5', '6', '7']
veiculos = [150, 170, 180, 160, 175, 185, 190]

# Criar o gráfico de barras
plt.bar(dias, veiculos, color='blue')

# Configurar título e rótulos dos eixos
plt.title('Quantidade de Veículos por Dia')
plt.xlabel('Dia')
plt.ylabel('Quantidade de Veículos')

# Mostrar o gráfico de barras
plt.show()
