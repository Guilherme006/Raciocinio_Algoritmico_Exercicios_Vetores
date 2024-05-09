notas = [10, 3, 8, 7.5, 4.8, 6, 9, 3.2, 7.8, 9.2, 6.1, 5.6, 7.3, 2.5, 0]

media = (notas[0] + notas[1] + notas[2] + notas[3] + notas[4] + notas[5] + notas[6] + notas[7] + notas[8] + notas[9] + notas[10] + notas[11] + notas[12] + notas[13] + notas[14]) / 15

print(f"A média geral é {media}")


# Outra forma de fazer
vetor = [0] * 15
indice = 0
soma = 0

while indice < 15:
    nota = float(input("Digite a sua nota: "))
    vetor[indice] = nota
    soma += nota
    indice += 1
    media = soma / 15

print(f"A média geral é {media}")