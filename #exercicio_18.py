#exercicio_18
import matplotlib.pyplot as plt
import numpy as np

# Dados de desempenho dos alunos (exemplo)
alunos = ['Ana', 'Bruno', 'Carlos', 'Diana', 'Eva']
notas = {
    'Ana': [8.0, 7.5, 9.0],
    'Bruno': [6.5, 7.0, 8.5],
    'Carlos': [7.0, 8.0, 7.5],
    'Diana': [9.0, 8.5, 9.5],
    'Eva': [6.0, 6.5, 7.0]
}
provas = ['Prova 1', 'Prova 2', 'Prova 3']

# Criar o gráfico de radar
def plot_radar(notas, alunos, provas):
    # Número de variáveis
    num_vars = len(provas)
    
    # Ângulos para cada variável
    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
    
    # O gráfico de radar deve ser circular, portanto, vamos "fechar o círculo"
    angles += angles[:1]
    
    # Inicializar o gráfico
    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
    
    # Desenhar uma linha para cada aluno
    for aluno in alunos:
        valores = notas[aluno]
        valores += valores[:1]  # fechar o círculo
        ax.plot(angles, valores, label=aluno)
        ax.fill(angles, valores, alpha=0.25)
    
    # Adicionar rótulos
    ax.set_yticklabels([])
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(provas)
    
    # Adicionar legenda
    ax.legend(loc='upper right', bbox_to_anchor=(1.1, 1.1))

    # Adicionar título
    plt.title('Desempenho dos Alunos nas Três Provas')
    
    plt.show()

# Plotar o gráfico de radar
plot_radar(notas, alunos, provas)
# Número de variáveis num_vars = len(provas) # Ângulos para cada variável angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
