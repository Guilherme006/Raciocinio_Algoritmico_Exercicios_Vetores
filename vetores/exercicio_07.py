vetor = [5, 10, 23, 100, -6, 7, 46, 14, 231, -15]

indice = 0
maior = 0
posicao = 0

while indice < 10:

    if vetor[indice] > maior:
        maior = vetor[indice]
        posicao = indice
    
    indice += 1
    

print(f"Vetor: {vetor}")
print(f"O maior número é {maior}")
print(f"A posição do maior número é {posicao}")
