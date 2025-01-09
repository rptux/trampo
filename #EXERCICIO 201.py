#EXERCICIO 201
import matplotlib.pyplot as plt

# Dados da tabela
meses = [1, 2, 3, 4, 5]
quantidade = [50, 60, 70, 80, 90]

# Plotar os pontos
plt.scatter(meses, quantidade, color='blue', label='Pontos da Tabela')

# Ajustar a linha reta
x = list(range(1, 6))
y = [10 * i + 40 for i in x]
plt.plot(x, y, color='red', label='y = 10x + 40')

# Configurar título e rótulos dos eixos
plt.title('Quantidade Vendida ao Longo dos Meses')
plt.xlabel('Mês')
plt.ylabel('Quantidade Vendida')
plt.legend()

# Mostrar o gráfico
plt.show()
