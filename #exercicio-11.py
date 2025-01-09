#exercicio-11
import matplotlib.pyplot as plt
import numpy as np

# Dados de crescimento populacional (exemplo)
anos = np.array([2020, 2021, 2022, 2023, 2024])
populacao = 5000 * (anos - 2020) + 20000  # P(x) = 5000x + 20000, com x = anos - 2020

# Criar o gráfico
plt.figure(figsize=(10, 5))
plt.plot(anos, populacao, marker='o', linestyle='-', color='b')

# Adicionar título e rótulos aos eixos
plt.title('Crescimento Populacional ao Longo dos Anos')
plt.xlabel('Ano')
plt.ylabel('População (habitantes)')

# Adicionar grade
plt.grid(True)

# Mostrar o gráfico
plt.show()
