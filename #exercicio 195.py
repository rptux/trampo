#exercicio 195
# Receber uma lista de números
numeros = list(map(int, input("Digite uma lista de números separados por espaço: ").split()))

# Inicializar o maior número como o primeiro número da lista
maior_numero = numeros[0]

# Encontrar o maior número na lista
for numero in numeros:
    if numero > maior_numero:
        maior_numero = numero

# Exibir o maior número
print("O maior número da lista é:", maior_numero)
