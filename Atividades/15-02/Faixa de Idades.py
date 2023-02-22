idade = int(input('Digite sua idade: '))
if idade >= 0 and idade < 10:
    print('Você é criança')
elif idade >= 10 and idade < 20:
    print('Você é adolescente')
elif idade >= 20 and idade < 30:
    print('Você é jovem')
elif idade >= 30 and idade <= 100:
    print('Você é adulto')
else:
    print('Valor não encontrado')