valor = int(input("Digite um valor: "))

vetor = [valor, valor, valor, valor, valor, valor, valor, valor, valor, valor]

indice = 0

maior = valor
menor = valor



while indice < 9:

    valor = int(input("Digite um valor: "))

    if valor > maior:
        maior = valor
    elif valor < menor:
        menor = valor

    indice += 1

print(f"O maior número é {maior}")
print(f"O menor número é {menor}")