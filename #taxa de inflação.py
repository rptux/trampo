#taxa de inflação
def calcular_media_taxa_inflacao(taxas):
    # Calcula a média das taxas de inflação
    media = sum(taxas) / len(taxas)
    return media

def calculadora_taxa_inflacao():
    print("Calculadora de Taxa de Inflação Mensal")
    print("Insira as taxas de inflação para cada mês. Digite 'sair' para finalizar a inserção.")

    taxas_inflacao = []

    while True:
        entrada = input("Digite a taxa de inflação (em %), ou 'sair' para finalizar: ")

        if entrada.lower() == 'sair':
            break

        try:
            taxa = float(entrada)
            taxas_inflacao.append(taxa)
        except ValueError:
            print("Por favor, insira um valor numérico válido.")

    if taxas_inflacao:
        media_taxa_inflacao = calcular_media_taxa_inflacao(taxas_inflacao)
        print(f"\nTaxas de Inflação Inseridas: {taxas_inflacao}")
        print(f"Média da Taxa de Inflação Mensal: {media_taxa_inflacao:.2f}%")
    else:
        print("Nenhuma taxa de inflação foi inserida.")

# Executar a calculadora
calculadora_taxa_inflacao()

