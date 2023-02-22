valores = []
n = int(input('Escreva a quantidade de números: '))
for x in range(n):
    valoresX=int(input('Escreva o número: '))
    valores.append(valoresX)

for x in range(len(valores)):
    if (valores[x]%2 == 0):
        print (valores[x],'é par')
    else:
        print (valores[x],'é ímpar')
