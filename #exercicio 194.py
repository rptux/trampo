#exercicio 194
# Receber um número
n = int(input("Digite um número: "))

# Inicializar o fatorial como 1
fatorial = 1

# Calcular o fatorial
for i in range(1, n + 1):
    fatorial *= i

# Exibir o fatorial
print("O fatorial de", n, "é:", fatorial)
