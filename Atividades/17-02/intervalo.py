def questao2():
    quantidade =0
    for i in range(10):
        numero =int(input('Digite o número: '))
        if numero >= 10 and numero <=50:
            quantidade = quantidade +1
            print(numero)

    print('números dentro do intervalo: ',quantidade)
questao2()