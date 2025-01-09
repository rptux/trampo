#grafico 1
import matplotlib.pyplot as plt

# Dados de preço (exemplo)
meses = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
precos = [50, 55, 60, 65, 60, 58, 62, 68, 70, 72, 70, 68]

# Criar o gráfico
plt.figure(figsize=(10, 5))
plt.plot(meses, precos, marker='o', linestyle='-', color='b')

# Adicionar título e rótulos aos eixos
plt.title('Variação do Preço de um Produto ao Longo do Ano')
plt.xlabel('Meses')
plt.ylabel('Preço (R$)')

# Adicionar grade
plt.grid(True)

# Mostrar o gráfico
plt.show()
