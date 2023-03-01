numeros=[]
contador=0
soma=0
for x in range(4):
    numeros.append(int(input('Digite as notas')))
for x in range(len(numeros)):
    soma = soma +  numeros[x]
print(soma)