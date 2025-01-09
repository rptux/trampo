#exercicio 175 dispersão
import matplotlib.pyplot as plt

# Dados do exercício 175
horas_estudadas = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
notas_obtidas = [65, 70, 75, 80, 85, 90, 95, 100, 105, 110]

# Criar o gráfico de dispersão
plt.scatter(horas_estudadas, notas_obtidas, color='blue', marker='o')

# Configurar título e rótulos dos eixos
plt.title('Gráfico de Dispersão: Horas Estudadas vs Notas Obtidas')
plt.xlabel('Horas Estudadas')
plt.ylabel('Notas Obtidas')

# Mostrar o gráfico de dispersão
plt.show()
