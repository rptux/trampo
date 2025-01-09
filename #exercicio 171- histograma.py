#exercicio 171- histograma
import matplotlib.pyplot as plt

# Dados do exercício 171
visitantes = [50, 55, 60, 65, 55, 70, 75, 80, 55, 90, 95, 100, 55, 110, 115, 120, 125, 55, 130, 135, 140, 145, 55, 150, 155, 160, 165, 170, 175, 180]

# Criar o histograma
plt.hist(visitantes, bins=14, edgecolor='black')

# Configurar título e rótulos dos eixos
plt.title('Histograma de Visitantes')
plt.xlabel('Número de Visitantes')
plt.ylabel('Frequência')

# Mostrar o histograma
plt.show()
