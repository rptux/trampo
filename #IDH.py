#IDH
# Dados dos países fictícios
paises = {
    'Pais A': {'expectativa_vida': 75, 'anos_esperados_escolaridade': 15, 'media_anos_estudo': 10, 'pib_per_capita': 20000},
    'Pais B': {'expectativa_vida': 70, 'anos_esperados_escolaridade': 14, 'media_anos_estudo': 9, 'pib_per_capita': 18000},
    'Pais C': {'expectativa_vida': 80, 'anos_esperados_escolaridade': 16, 'media_anos_estudo': 12, 'pib_per_capita': 25000}
}

# Fórmula para calcular o IDH
def calcular_idh(expectativa_vida, anos_esperados_escolaridade, pib_per_capita):
    idh_vida = expectativa_vida / 85
    idh_educacao = anos_esperados_escolaridade / 20
    idh_renda = pib_per_capita / 40000
    idh = (idh_vida + idh_educacao + idh_renda) / 3
    return idh

# Calculando o IDH para cada país
for pais, dados in paises.items():
    idh = calcular_idh(dados['expectativa_vida'], dados['anos_esperados_escolaridade'], dados['pib_per_capita'])
    print(f"IDH do {pais}: {idh:.4f}")
