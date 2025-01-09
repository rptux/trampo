#grafico desemprego
import matplotlib.pyplot as plt

# Dados da taxa de desemprego (exemplo)
anos = ['2019', '2020', '2021', '2022', '2023']
taxa_desemprego = [8.5, 9.0, 10.2, 9.8, 8.7]

# Criar o gráfico
plt.figure(figsize=(10, 5))
plt.plot(anos, taxa_desemprego, marker='o', linestyle='-', color='r')

# Adicionar título e rótulos aos eixos
plt.title('Taxa de Desemprego ao Longo dos Últimos 5 Anos')
plt.xlabel('Anos')
plt.ylabel('Taxa de Desemprego (%)')

# Adicionar grade
plt.grid(True)

# Mostrar o gráfico
plt.show()
