print('\nTabuada de Multiplicação de 13\n')
for x in range (10):
    print (f'A multiplicação de',(x+1),'é igual a: ',(x+1)*13)

print('\nTabuada de Divisão de 13\n')
for x in range (10):
    # variavel = (x+1)/13
    # variavelTexto = "{0:.2f}".format(variavel)
    # print(variavelTexto)
    print (f'A divisão de {(x+1)} é igual a: {((x+1)/13):,.2f}')

print('\nTabuada de Soma de 13\n')
for x in range (10):
    print (f'A soma de',(x+1),'é igual a: ',(x+1)+13)

print('\nTabuada de Subtração de 13\n')
for x in range (10):
    print (f'A subtração de',(x+1),'é igual a: ',(x+1)-13)