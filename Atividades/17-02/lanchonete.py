#Mostrar o cardápio
print("100 - Hot Dog - R$ 1,10")
print("101 - Hot Dog - R$ 1,40")
print("102 - Hot Dog - R$ 1,50")
#Definir o valor através do codígo do lanche
while True:
    codigo = int(input("Digite o código do seu pedido:"))
    quantidade = int(input("Digite a quantidade: "))
    if codigo == 100:
        valor = 1.10
        break
    elif codigo == 101: 
        valor = 1.40
        break
    elif codigo == 102: 
        valor = 1.50
        break
    else:
        print ('Codigo invalido')
#Calcular e mostrar o valor total do lanche
total = valor*quantidade
print (f'O Valor total do pedido é: R$ {total:,.2f}')