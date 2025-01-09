#exercicio 180 gráfico de pizza
import matplotlib.pyplot as plt

# Dados do exercício 180
notas = ['A', 'B', 'C', 'D']
frequencias = [5, 7, 6, 2]

# Criar o gráfico de pizza
plt.pie(frequencias, labels=notas, autopct='%1.1f%%', startangle=90, colors=['lightblue', 'lightgreen', 'lightcoral', 'lightskyblue'])

# Configurar título
plt.title('Distribuição das Notas dos Alunos')

# Mostrar o gráfico de pizza
plt.show()
