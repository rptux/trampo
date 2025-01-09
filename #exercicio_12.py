#exercicio_12
import matplotlib.pyplot as plt
import numpy as np

# Dados da taxa de desemprego (exemplo)
anos = np.array([2021, 2022, 2023, 2024, 2025])
anos_offset = anos - 2020  # Anos após 2020
taxa_desemprego = -0.5 * anos_offset + 10  # T(x) = -0.5x + 10, com x = anos_offset

# Criar o gráfico
plt.figure(figsize=(10, 5))
plt.plot(anos, taxa_desemprego, marker='o', linestyle='-', color='r')

# Adicionar título e rótulos aos eixos
plt.title('Taxa de Desemprego ao Longo dos Anos')
plt.xlabel('Ano')
plt.ylabel('Taxa de Desemprego (%)')

# Adicionar grade
plt.grid(True)

# Mostrar o gráfico
plt.show()
