#grafico exercicio 6 - desemprego
import matplotlib.pyplot as plt

# Dados de crescimento populacional (exemplo)
anos = ['2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023']
populacao = [20010, 21020, 22358, 23110, 24503, 26210, 28032, 30036, 32000, 35050]

# Criar o gráfico
plt.figure(figsize=(10, 5))
plt.plot(anos, populacao, marker='o', linestyle='-', color='g')

# Adicionar título e rótulos aos eixos
plt.title('Crescimento Populacional ao Longo de uma Década')
plt.xlabel('Ano')
plt.ylabel('População')

# Adicionar grade
plt.grid(True)

# Mostrar o gráfico
plt.show()
