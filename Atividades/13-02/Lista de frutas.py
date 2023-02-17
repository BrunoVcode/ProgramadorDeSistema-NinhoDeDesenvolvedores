frutas = []
valor1 = 1
for x in range(5):
    frutaX = input('Escreva o nome da fruta '+str(x+1)+(': '))
    frutas.append(frutaX)
print ('A fruta:', frutas[0],'custa: R$', (valor1))
print ('A fruta:', frutas[1],'custa: R$', (valor1*2))
print ('A fruta:', frutas[2],'custa: R$', (valor1/2))
print ('A fruta:', frutas[3],'custa: R$', ((valor1/2)*3))
print ('A fruta:', frutas[4],'custa: R$', (((valor1/2)*3)/2))