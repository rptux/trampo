#taxa de variações - população
import matplotlib.pyplot as plt

# Dados de crescimento populacional (exemplo)
anos = ['2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023']
populacao = [20000, 21000, 22000, 23000, 24500, 26000, 28000, 30000, 32000, 35000]

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
