frutas = []
valores = [1, 1*2, 1/2, (1/2)*3, ((1/2)*3)/2]
for x in range(5):
    frutasX = input('Escreva o nome da fruta '+str(x+1)+': ')
    frutas.append(frutasX)
for x in range(5):
    print(f'A fruta', frutas[x], 'custa R$', valores[x])
