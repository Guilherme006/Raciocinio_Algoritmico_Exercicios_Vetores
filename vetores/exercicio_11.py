vetor = [5, -10, 23, 100, -6,]

indice = 0
maior = 0
menor = 0
posicao_maior = 0
posicao_menor = 0

while indice < 5:

    if vetor[indice] > maior:
        maior = vetor[indice]
        posicao_maior = indice
    elif vetor[indice] < menor:
        menor = vetor[indice]
        posicao_menor = indice
    
    
    indice += 1
    

print(f"Os valores são {vetor}, a posição do maior valor é {posicao_maior} e a posição do menor valor é {posicao_menor}!")