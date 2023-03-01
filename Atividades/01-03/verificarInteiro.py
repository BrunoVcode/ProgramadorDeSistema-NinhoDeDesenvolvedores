try:  
    n= int(input('Escreva um número: '))  
    print(f'O número {n} é inteiro')  
except ValueError as err:  
    print(err)  
 