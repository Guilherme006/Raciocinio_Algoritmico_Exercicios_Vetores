valores = [15, -8, 25, 32, 2]

media = (valores[0] + valores[1] + valores[2] + valores[3] + valores[4] / 5)

indice = 0
maior = valores[indice]
menor = valores[indice]


while indice < 5:
    if valores[indice] > maior:
        maior = valores[indice]
    elif valores[indice] < menor:
        menor = valores[indice]
    
    indice += 1

print(f"Os valores são {valores}, o maior número é {maior} e o menor número é {menor}!")