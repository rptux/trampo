#exercicio_16
import matplotlib.pyplot as plt

# Dados de gastos (exemplo)
meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho']
alimentacao = [800, 850, 900, 850, 800, 750]
moradia = [1200, 1200, 1200, 1200, 1200, 1200]
transporte = [300, 320, 350, 340, 330, 320]
lazer = [200, 220, 250, 230, 210, 200]

# Criar o gráfico
plt.figure(figsize=(10, 5))

# Plotando cada categoria de gastos
plt.plot(meses, alimentacao, marker='o', linestyle='-', label='Alimentação')
plt.plot(meses, moradia, marker='o', linestyle='-', label='Moradia')
plt.plot(meses, transporte, marker='o', linestyle='-', label='Transporte')
plt.plot(meses, lazer, marker='o', linestyle='-', label='Lazer')

# Adicionar título e rótulos aos eixos
plt.title('Variação dos Gastos Mensais por Categoria')
plt.xlabel('Meses')
plt.ylabel('Gastos (R$)')

# Adicionar legenda
plt.legend()

# Adicionar grade
plt.grid(True)

# Mostrar o gráfico
plt.show()
