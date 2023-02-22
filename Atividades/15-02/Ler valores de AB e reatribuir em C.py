valores = []
for x in range(2):
    valoresX=int(input('Escreva o número: '))
    valores.append(valoresX)
soma=(valores[0]+valores[1])
mult=(valores[0]*valores[1])
if (valores[0]==valores[1]):
    c = soma
else:
    c = mult
print('C é igual a:',c)

