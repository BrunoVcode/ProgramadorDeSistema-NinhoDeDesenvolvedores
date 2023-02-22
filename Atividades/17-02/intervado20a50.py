numeros = []
for x in range (10):
    numerosX = int(input('Digite os números que deseja verificar: '))
    if numeros >= 10 and numeros <=50:
        numeros.append(numerosX)
for x in range(len(numeros)):
    print (numeros[x])
        
