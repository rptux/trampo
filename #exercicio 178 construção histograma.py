#exercicio 178 construção histograma
import matplotlib.pyplot as plt

# Dados do exercício 178
tempos = [30, 32, 28, 35, 30, 32, 28, 34, 31, 30, 33, 29, 30, 31, 33, 30, 32, 34, 30, 29]

# Criar o histograma
plt.hist(tempos, bins=8, edgecolor='black')

# Configurar título e rótulos dos eixos
plt.title('Histograma de Tempos para Completar Tarefa')
plt.xlabel('Tempo (minutos)')
plt.ylabel('Frequência')

# Mostrar o histograma
plt.show()
