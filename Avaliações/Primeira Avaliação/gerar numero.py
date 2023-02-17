numero = int(input('escreva um número inteiro positivo com três dígitos: '))
numeroGerado = (numero % 10*100)+(numero//10 % 10*10)+(numero//10//10)
print('O número gerado foi: ', numeroGerado)
