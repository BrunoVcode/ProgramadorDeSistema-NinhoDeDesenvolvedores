numeros=[10,7,12,8]
for x in range(len(numeros)):
    if x == 0:
        maior = numeros[x]
    if numeros[x] > maior:
        maior = numeros[x]
print (maior)