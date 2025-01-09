# exercicio 172 box-plot
import matplotlib.pyplot as plt

# Dados do exercício 172
tempos_corrida = [150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290]

# Criar o box-plot
plt.boxplot(tempos_corrida, vert=False)

# Configurar título e rótulos dos eixos
plt.title('Box-Plot de Tempos de Corrida')
plt.xlabel('Tempo (minutos)')

# Mostrar o box-plot
plt.show()
