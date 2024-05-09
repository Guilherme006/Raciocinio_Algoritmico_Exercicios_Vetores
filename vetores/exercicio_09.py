valores = [-1, -2, -3, -4, -5, 6, 7, 8, 9, 10]

numeros_negativos = 0
indice = 0
soma = 0

while indice < 10:
    if valores[indice] < 0:
        numeros_negativos += 1
    else:
        soma += valores[indice]
    
    indice += 1

print(f"A quantidade de números negativos é {numeros_negativos}")
print(f"A soma dos números positivos é {soma}")
