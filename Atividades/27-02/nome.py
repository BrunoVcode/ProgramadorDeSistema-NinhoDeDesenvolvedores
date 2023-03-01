from rich.console import Console
console = Console()
print('Escreva um nome')
nome=str(input('> '))
print(f'A quantidade de letras do nome {nome} é igual a {len(nome)}')
print(f'A primeira letra do nome de {nome} é {nome[0]}')
nomeInvertido=(nome[::-1])
print(f'O nome {nome} ao contrario é ', end='')
print((nomeInvertido.capitalize()))
nomeLetras=[]
for x in range(len(nome)):
    if x % 2 == 0:
        nomeLetras.append(nome[x])
print(f'As letras ímpares de {nome}, são ', end='')
print (*nomeLetras, sep=', ')

