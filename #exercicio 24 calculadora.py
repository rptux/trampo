#exercicio 24 calculadora
def anos_luz_para_metros(anos_luz):
    # 1 ano-luz = 9.461 * 10^15 metros
    metros = anos_luz * 9.461 * 10**15
    return metros

def parsecs_para_metros(parsecs):
    # 1 parsec = 3.086 * 10^16 metros
    metros = parsecs * 3.086 * 10**16
    return metros

def metros_para_kilometros(metros):
    # 1 metro = 10^-3 quilômetros
    kilometros = metros * 10**-3
    return kilometros

def calculadora_distancias():
    print("Calculadora de Conversão de Distâncias Astronômicas")
    
    print("\nOpções:")
    print("1. Anos-luz para Metros")
    print("2. Parsecs para Metros")
    print("3. Metros para Quilômetros")
    print("4. Sair")
    
    while True:
        opcao = int(input("\nEscolha uma opção: "))
        
        if opcao == 1:
            anos_luz = float(input("Digite a distância em anos-luz: "))
            metros = anos_luz_para_metros(anos_luz)
            print(f"{anos_luz} anos-luz são aproximadamente {metros:.3e} metros.")
        
        elif opcao == 2:
            parsecs = float(input("Digite a distância em parsecs: "))
            metros = parsecs_para_metros(parsecs)
            print(f"{parsecs} parsecs são aproximadamente {metros:.3e} metros.")
        
        elif opcao == 3:
            metros = float(input("Digite a distância em metros: "))
            kilometros = metros_para_kilometros(metros)
            print(f"{metros:.3e} metros são aproximadamente {kilometros:.3e} quilômetros.")
        
        elif opcao == 4:
            print("Encerrando a calculadora.")
            break
        
        else:
            print("Opção inválida! Tente novamente.")

# Executar a calculadora
calculadora_distancias()
