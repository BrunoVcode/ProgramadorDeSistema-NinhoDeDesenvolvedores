from rich.console import Console
console = Console()
print('Escreva um nome')
nome=str(input('> '))
print(f'A quantidade de letras do nome {nome} é igual a {len(nome)-nome.count(" ")}')
print(f'A primeira letra do nome de {nome} é {nome[0]}')
# nomeInvertido=(nome[::-1])
# print(f'O nome {nome} ao contrario é ', end='')
# nomeInvertidoEditado = nomeInvertido.capitalize()
# console.print(nomeInvertidoEditado, style='red b ')
nomeInvertido = ''
for x in range(len(nome)):
    nomeInvertido = nomeInvertido + nome[len(nome)-1-x]
nomeInvertidoEditado = nomeInvertido.capitalize()
print(f'O nome {nome} ao contrario é ', end='')
console.print (nomeInvertidoEditado, style='red b ')
nomeLetras=[]
for x in range(len(nome)):
    if (x+1) % 2 != 0:
        nomeLetras.append(nome[x])
print(f'As letras ímpares de {nome}, são ', end='')
print (*nomeLetras, sep=', ')