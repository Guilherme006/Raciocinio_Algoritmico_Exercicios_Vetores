import random

apostas = [0, 0, 0, 0, 0, 0]

sorteio = [random.randint(6,50), random.randint(6,50), random.randint(6,50), random.randint(6,50), random.randint(6,50), random.randint(6,50)]

indice = 0

acertos = 0


while indice < 6:
    numeros = int(input("Qual sua aposta: "))
    apostas[indice] = numeros
    indice += 1

    if apostas == sorteio:
        acertos += 1

print(f"Os numeros apostados foram: {apostas}")
print(f"Os numeros sorteados foram: {sorteio}")
print(f"A quantidade de acertos foi: {acertos}")



    