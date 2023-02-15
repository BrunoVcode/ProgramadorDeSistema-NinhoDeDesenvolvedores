# Modulos importados
import time
import sys
from pokemonsClass import *
from trerinadorClass import *
# Logo em ASCII
print("""\
                                  ,'|
    _.----.        ____         ,'  _\   ___    ___     ____
_,-'       `.     |    |  /`.   \,-'    |   \  /   |   |    \  |`.
\      __    \    '-.  | /   `.  ___    |    \/    |   '-.   \ |  |
 \.    \ \   |  __  |  |/    ,','_  `.  |          | __  |    \|  |
   \    \/   /,' _`.|      ,' / / / /   |          ,' _`.|     |  |
    \     ,-'/  /   \    ,'   | \/ / ,`.|         /  /   \  |     |
     \    \ |   \_/  |   `-.  \    `'  /|  |    ||   \_/  | |\    |
      \    \ \      /       `-.`.___,-' |  |\  /| \      /  | |   |
       \    \ `.__,'|  |`-._    `|      |__| \/ |  `.__,'|  | |   |
        \_.-'       |__|    `-._ |              '-.|     '-.| |   |
                                `'                            '-._|
    """)

# Codigo para deixar o Texto lento


def slowprint(texto, atraso=0.05):
    for x in texto:
        print(x, end='', flush=True)
        time.sleep(atraso)


print(charmander.ataques, charmander.hp)
# Introdução
slowprint('Olá, bem vindo ao mundo pokémon.\nEspero que se divirta!!!\n')
nome = input('\nQual o seu nome? ')
slowprint('\nVocê acorda em uma estrada e vê um homen sendo atacado por um Pokémon selvagem!!!\n')

# Escolha 01
escolha01 = input("""
    Escolha o que você quer fazer:

    1. Fugir
    2. Ajudar
    """)
if escolha01.lower() == "1":
    slowprint(
        '\nVocê tenta fugir, mas cai e bate a cabeça em uma pedra. \nFIM DE JOGO!')
    sys.exit()
elif escolha01.lower() == "2":
    slowprint('\nVocê vê uma bolsa com 3 poquebolas proximas a ela.')

# Escolha 02
while True:
    escolha02 = input("""
    Escolha o que você quer fazer:

    1. Falar com o homem
    2. Pegar uma das pokebolas
    """)
    if escolha02.lower() == "1":
        slowprint(
            '\nO homen grita: -SOCORRO!!! ME AJUDA!!!\n')
    else:
        break
slowprint('\nQual Pokebola você escolhe?\n')
# Escolha 03 - Escolha do Pókemon inicial
escolha03 = input("""
    Escolha o que você quer fazer:

    1. Pegar a pokebola azul
    2. Pegar a pokebola vermelha
    3. Pegar a pokebola verde
    """)
if escolha03 == "1":
    slowprint('\nVocê pega a pokebola azul. \nE dela sai um Squirtle!!!\n')
elif escolha03 == "2":
    slowprint('\nVocê pega a pokebola vermelha. \nE dela sai um Charmander!!!\n')
else:
    slowprint('\nVocê pega a pokebola verde. \nE dela sai um Bulbasaur!!!\n')
slowprint('\nDê um Comando para o seu novo Pokémon!!!.\n')

# batalha 01
while True:
    batalha01 = input("""
    Escolha o que você quer fazer:

    1. Atacar
    2. Defender
    """)
    if batalha01 == "2":
        slowprint(
            '\nO seu Pokémon se defendeu.\nO homen continua sendo atacado D:\n')
    else:
        break
slowprint('\nO seu Pokémon atacou.\n')
slowprint('\nO Pokémon selvagem foge.\nVocê venceu a batalha!!!')
