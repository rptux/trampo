#calculadora volume esferico
import math

def calcular_volume_esfera(raio):
    # Volume da esfera: V = 4/3 * pi * r^3
    volume = (4 / 3) * math.pi * raio**3
    return volume

def calcular_area_superficie_esfera(raio):
    # Área da superfície da esfera: A = 4 * pi * r^2
    area = 4 * math.pi * raio**2
    return area

def calculadora_reservatorio():
    print("Calculadora de Volume de Reservatório Esférico")

    # Entrada do raio da esfera
    raio = float(input("Digite o raio do reservatório (em metros): "))

    # Calcular o volume e a área da superfície
    volume = calcular_volume_esfera(raio)
    area_superficie = calcular_area_superficie_esfera(raio)

    # Entrada dos custos
    custo_volume = float(input("Digite o custo por metro cúbico de volume armazenado (em R$): "))
    custo_revestimento = float(input("Digite o custo por metro quadrado de revestimento da superfície interna (em R$): "))

    # Calcular os custos
    custo_total_volume = volume * custo_volume
    custo_total_revestimento = area_superficie * custo_revestimento
    custo_total = custo_total_volume + custo_total_revestimento

    # Exibir resultados
    print(f"\nVolume do reservatório: {volume:.2f} metros cúbicos")
    print(f"Área da superfície interna do reservatório: {area_superficie:.2f} metros quadrados")
    print(f"Custo total de construção do reservatório: R$ {custo_total:.2f}")

# Executar a calculadora
calculadora_reservatorio()
