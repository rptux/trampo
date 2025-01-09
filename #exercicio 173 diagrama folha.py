#exercicio 173 diagrama folha
import pandas as pd

# Dados do exercício 173
notas = [75, 80, 85, 90, 80, 70, 85, 95, 85, 100, 80, 75, 85, 90, 95]

# Criar uma Série do pandas com os dados
serie_notas = pd.Series(notas)

# Criar o diagrama de ramos e folhas
def stem_and_leaf(series):
    series_sorted = sorted(series)
    stems = {}
    for number in series_sorted:
        stem = number // 10
        leaf = number % 10
        if stem in stems:
            stems[stem].append(leaf)
        else:
            stems[stem] = [leaf]
    
    for stem, leaves in stems.items():
        print(f'{stem} | {" ".join(map(str, leaves))}')

# Exibir o diagrama de ramos e folhas
print("Diagrama de Ramos e Folhas:")
stem_and_leaf(serie_notas)
