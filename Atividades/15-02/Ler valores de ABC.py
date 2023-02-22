valores = []
for x in range(3):
    valoresX=int(input('Escreva o número: '))
    valores.append(valoresX)
ab=(valores[0]+valores[1])
if (ab < valores[2]):
    print ('O Valor de A + B é menor que C')
else:
    print ('O Valor de A + B é maior que C')
