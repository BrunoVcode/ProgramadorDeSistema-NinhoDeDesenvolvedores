# Modulos importados
import time
import sys
import random
import os
from pokemonsClass import *
# Limpar tela
def clear(): return os.system('cls')


clear()

# Logo em ASCII
print("""
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
""""
Use o print para imprimir caractere por caractere e sleep para criar uma pausa entre cada caractere.
Nesse caso para print é passado o argumento '' para o parâmetro end significando que ao final da impressão não será pulada uma linha.
Para o parâmetro flush é passado o argumento True pois print usa um buffer de saída e o parâmetro flush indica que esse buffer deva
ser despejado ou não após a evocação do comando e um valor True indica que sim deva ser despejado. Se não fosse feito assim a impressão
só seria feita após o término do loop que contém a instrução
A função print usa de um buffer da dados para optimizar a impressão. Quando faz flush=True estou informando a função que descarregue
imediatamente o conteúdo desse buffer na saída. Caso não fizesse a impressão só ocorreria quando terminasse o laço for que contém a função.
"""


def slowprint(texto, atraso=0.05):
    for x in texto:
        print(x, end='', flush=True)
        time.sleep(atraso)


# Introdução
time.sleep(0.5)
print("""
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓""")
slowprint("""                Olá, bem vindo ao mundo pokémon.\n                    Espero que se divirta!!!\n""")
print("""┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛""")


time.sleep(1)
slowprint('\nVocê acorda em uma estrada e vê um homen sendo atacado por um Pokémon selvagem!!!\n')

# Escolha 01
time.sleep(0.5)
print("""
    Escolha o que você quer fazer:

    1. Fugir
    2. Ajudar
    """)
escolha01 = input('> ')
if escolha01.lower() == "1":
    slowprint(
        '\nVocê tenta fugir, mas cai e bate a cabeça em uma pedra. \nFIM DE JOGO!')
    sys.exit()
elif escolha01.lower() == "2":
    slowprint('\nVocê vê uma bolsa com 3 poquebolas proximas a ela.')

# Escolha 02
while True:
    print("""
    Escolha o que você quer fazer:

    1. Falar com o homem
    2. Pegar uma das pokebolas
    """)
    escolha02 = input('> ')
    if escolha02.lower() == "1":
        slowprint(
            '\nO homen grita: -SOCORRO!!! ME AJUDA!!!\n')
    else:
        break
slowprint('\nQual Pokebola você escolhe?\n')
# Escolha 03 - Escolha do Pókemon inicial
print("""
    Escolha o que você quer fazer:

    1. Pegar a pokebola azul
    2. Pegar a pokebola vermelha
    3. Pegar a pokebola verde
    """)
escolha03 = input('> ')
if escolha03 == "1":
    slowprint('\nVocê pega a pokebola azul. \nE dela sai um Squirtle!!!\n')
    principal = squirtle.nome
    principalTipo = aAgua
elif escolha03 == "2":
    slowprint('\nVocê pega a pokebola vermelha. \nE dela sai um Charmander!!!\n')
    principal = charmander.nome
    principalTipo = aFogo
else:
    slowprint('\nVocê pega a pokebola verde. \nE dela sai um Bulbasaur!!!\n')
    principal = bulbasaur.nome
    principalTipo = aGrama
slowprint('\nDê um Comando para o Pokémon!!!\n')


# Variaveis
inventario = []
hp = 10
hpInimigo = 10
pokemonSelvagem = charmander
inimigoTipo = aFogo

# batalha 01 - definição do inimigo
pokemonInimigo = random.randint(1, 3)
if pokemonInimigo == 1:
    pokemonSelvagem = charmander.nome
    inimigoTipo = aFogo
elif pokemonInimigo == 2:
    pokemonSelvagem = squirtle.nome
    inimigoTipo = aAgua
else:
    pokemonSelvagem = bulbasaur.nome
    inimigoTipo = aGrama

# batalha 01 - Ataques do pokemon principal
while hp > 0 and hpInimigo > 0:

    print('\n        Escolha o ataque:\n')

    print('        1. '+principalTipo[0])
    print('        2. '+principalTipo[1])
    print('        3. '+principalTipo[2])
    print('        4. '+principalTipo[3])
    batalhaPrincipal = input('\n> ')
    if batalhaPrincipal == "1":
        slowprint(principal + ' usou '+principalTipo[0])
        hpInimigo = hpInimigo - 1
    elif batalhaPrincipal == "2":
        slowprint(principal + ' usou '+principalTipo[1])
        hpInimigo = hpInimigo - 2
    elif batalhaPrincipal == "3":
        slowprint(principal + ' usou '+principalTipo[2])
        hpInimigo = hpInimigo - 3
    elif batalhaPrincipal == "4":
        slowprint(principal + ' usou '+principalTipo[3])
        hpInimigo = hpInimigo - 4
    else:
        slowprint(principal + ' fica confuso e não ataca')

    print('\nO HP do '+pokemonSelvagem+' selvagem agora é: ', hpInimigo)
    if hpInimigo <= 0:
        break
    # batalha 01 - Ataques do pokemon selvagem
    else:
        slowprint('\nO Pokémon te ataca')
        ataqueInimigo = random.randint(1, 4)
        if ataqueInimigo == 1:
            slowprint('\n'+pokemonSelvagem+' selvagem '+inimigoTipo[0])
            hp = hp - 1
        elif ataqueInimigo == 2:
            slowprint('\n'+pokemonSelvagem+' selvagem usou '+inimigoTipo[0])
            hp = hp - 2
        elif ataqueInimigo == 3:
            slowprint('\n'+pokemonSelvagem+' selvagem usou '+inimigoTipo[0])
            hp = hp - 3
        elif ataqueInimigo == 4:
            slowprint('\n'+pokemonSelvagem+' selvagem usou '+inimigoTipo[0])
            hp = hp - 4
        else:
            slowprint('\n'+pokemonSelvagem +
                      ' selvagem fica confuso e não ataca')
        print('\nO HP do seu pokémon agora é: ', hp)
if hpInimigo <= 0:
    slowprint(
        '\nVocê venceu\n')
elif hp <= 0:
    slowprint(
        '\nVocê foi derrotado\n')
slowprint('\nO '+pokemonSelvagem+' selvagem foge.\nVocê venceu a batalha!!!\n')
# Fim da batalha 01
slowprint(
    '\nHomen desconhecido: -Obrigado pela ajuda!!!\n-Qual o seu nome?\n')
nome = input('> ')
print('-', nome, end="")
slowprint(', como forma de agradecimento\nEsse Pokémon é seu!\n')
inventario.append(principal)
# Jornada do heroi
time.sleep(1.5)
slowprint('\nAgora você está na estrada e ganhou seu primeiro Pokémon!\n')

# Escolha05
while True:
    slowprint('\nVocê pode seguir por 3 caminhos diferentes\n')
    print("""
        Escolha o que você quer fazer:

        1. Ir para a esquerda
        2. Seguir em frente
        3. Ir para a direita
        """)

    hp = 10
    hpInimigo = 10
    escolha05 = input('> ')
    if escolha05 == "1":
        # batalha 02 - definição do inimigo
        pokemonInimigo = random.randint(1, 3)
        if pokemonInimigo == 1:
            pokemonSelvagem = charmander.nome
            inimigoTipo = aFogo
        elif pokemonInimigo == 2:
            pokemonSelvagem = squirtle.nome
            inimigoTipo = aAgua
        else:
            pokemonSelvagem = bulbasaur.nome
            inimigoTipo = aGrama
        # batalha 02 - Ataques do seu pokemon

        slowprint('\nVocê é atacado por um Pokémon selvagem.\n')
        while hp > 0 and hpInimigo > 0:

            print('\n        Escolha o ataque:\n')

            print('        1. '+principalTipo[0])
            print('        2. '+principalTipo[1])
            print('        3. '+principalTipo[2])
            print('        4. '+principalTipo[3])
            batalhaPrincipal = input('\n> ')
            if batalhaPrincipal == "1":
                slowprint(principal + ' usou '+principalTipo[0])
                hpInimigo = hpInimigo - 1
            elif batalhaPrincipal == "2":
                slowprint(principal + ' usou '+principalTipo[1])
                hpInimigo = hpInimigo - 2
            elif batalhaPrincipal == "3":
                slowprint(principal + ' usou '+principalTipo[2])
                hpInimigo = hpInimigo - 3
            elif batalhaPrincipal == "4":
                slowprint(principal + ' usou '+principalTipo[3])
                hpInimigo = hpInimigo - 4
            else:
                slowprint(principal + ' fica confuso e não ataca')

            print('\nO HP do '+pokemonSelvagem +
                  ' selvagem agora é: ', hpInimigo)
            if hpInimigo <= 0:
                break
        # batalha 02 - Ataques do pokemon selvagem
            else:
                slowprint('\nO Pokémon te ataca')
            ataqueInimigo = random.randint(1, 4)
            if ataqueInimigo == 1:
                slowprint('\n'+pokemonSelvagem+' selvagem '+inimigoTipo[0])
                hp = hp - 1
            elif ataqueInimigo == 2:
                slowprint('\n'+pokemonSelvagem +
                          ' selvagem usou '+inimigoTipo[0])
                hp = hp - 2
            elif ataqueInimigo == 3:
                slowprint('\n'+pokemonSelvagem +
                          ' selvagem usou '+inimigoTipo[0])
                hp = hp - 3
            elif ataqueInimigo == 4:
                slowprint('\n'+pokemonSelvagem +
                          ' selvagem usou '+inimigoTipo[0])
                hp = hp - 4
            else:
                slowprint('\n'+pokemonSelvagem +
                          ' selvagem fica confuso e não ataca')
            print('\nO HP do seu pokémon agora é: ', hp)
            if hpInimigo <= 0:
                slowprint(
                    '\nVocê venceu\n')
            elif hp <= 0:
                slowprint(
                    '\nVocê foi derrotado\n')

    elif escolha05 == "3":
        slowprint('\nVocê é atacado por um Pokémon selvagem.\n')
    # batalha 02 - definição do inimigo
        pokemonInimigo = random.randint(1, 3)
        if pokemonInimigo == 1:
            pokemonSelvagem = charmander.nome
            inimigoTipo = aFogo
        elif pokemonInimigo == 2:
            pokemonSelvagem = squirtle.nome
            inimigoTipo = aAgua
        else:
            pokemonSelvagem = bulbasaur.nome
            inimigoTipo = aGrama
        # batalha 02 - Ataques do seu pokemon

        while hp > 0 and hpInimigo > 0:

            print('\n        Escolha o ataque:\n')

            print('        1. '+principalTipo[0])
            print('        2. '+principalTipo[1])
            print('        3. '+principalTipo[2])
            print('        4. '+principalTipo[3])
            batalhaPrincipal = input('\n> ')
            if batalhaPrincipal == "1":
                slowprint(principal + ' usou '+principalTipo[0])
                hpInimigo = hpInimigo - 1
            elif batalhaPrincipal == "2":
                slowprint(principal + ' usou '+principalTipo[1])
                hpInimigo = hpInimigo - 2
            elif batalhaPrincipal == "3":
                slowprint(principal + ' usou '+principalTipo[2])
                hpInimigo = hpInimigo - 3
            elif batalhaPrincipal == "4":
                slowprint(principal + ' usou '+principalTipo[3])
                hpInimigo = hpInimigo - 4
            else:
                slowprint(principal + ' fica confuso e não ataca')

            print('\nO HP do '+pokemonSelvagem +
                  ' selvagem agora é: ', hpInimigo)
            if hpInimigo <= 0:
                break
        # batalha 02 - Ataques do pokemon selvagem
            else:
                slowprint('\nO Pokémon te ataca')
            ataqueInimigo = random.randint(1, 4)
            if ataqueInimigo == 1:
                slowprint('\n'+pokemonSelvagem+' selvagem '+inimigoTipo[0])
                hp = hp - 1
            elif ataqueInimigo == 2:
                slowprint('\n'+pokemonSelvagem +
                          ' selvagem usou '+inimigoTipo[0])
                hp = hp - 2
            elif ataqueInimigo == 3:
                slowprint('\n'+pokemonSelvagem +
                          ' selvagem usou '+inimigoTipo[0])
                hp = hp - 3
            elif ataqueInimigo == 4:
                slowprint('\n'+pokemonSelvagem +
                          ' selvagem usou '+inimigoTipo[0])
                hp = hp - 4
            else:
                slowprint('\n'+pokemonSelvagem +
                          ' selvagem fica confuso e não ataca')
            print('\nO HP do seu pokémon agora é: ', hp)
            if hpInimigo <= 0:
                slowprint(
                    '\nVocê venceu\n')
            elif hp <= 0:
                slowprint(
                    '\nVocê foi derrotado\n')

    elif escolha05 == "2":
        slowprint('\nVocê vê seu rival logo a frente.\n')
        break
    else:
        slowprint('\nVocê fica indeciso.....\n')
    hp = 10
    hpInimigo = 10
    # Capturar pokémon
    slowprint('\nVocê quer capturar '+pokemonSelvagem+' ?')
    print("""

        1. Sim
        2. Não
        """)
    capturar01 = input('> ')
    if capturar01 == '1':
        inventario.append(pokemonSelvagem)
        slowprint('\nVocê capturou '+pokemonSelvagem)
    else:
        slowprint('\nVocê não capturou '+pokemonSelvagem)

    print("""
        \nEscolha o que você quer fazer:

        1. Verificar Pokebolas\n
        2. Sair do jogo
        """)
    escolha06 = input('> ')
    if escolha06 == "1":
        slowprint('\nPokémons disponiveis:\n')

        for x in range(len(inventario)):
            print(inventario[x])
        slowprint(
            '\nEscreva o nome do seu Pokémon principal (com letras em minusculo):\n')

    # Escolher entre os pokemons das pokebolas
        while True:
            inventarioP = input('> ')
            if inventarioP == ('bulbasaur'):
                principal = bulbasaur.nome
                principalTipo = aGrama
                slowprint('\nSeu Pokémon principal é Bulbasaur.\n')
                break
            elif inventarioP == ('charmander'):
                principal = charmander.nome
                principalTipo = aFogo
                slowprint('\nSeu Pokémon principal é Charmander.\n')
                break
            elif inventarioP == ('squirtle'):
                pokemonSelvagem = squirtle.nome
                inimigoTipo = aAgua
                slowprint('\nSeu Pokémon principal é Squirtle.\n')
                break
            else:
                print('Nome escrito invalido, tente novamente.')
    else:
        slowprint('\nFechando o jogo...\n')
# batalha rival
slowprint('\nSeu Rival te chama para uma batalha!!!.\n')
slowprint('Qual o nome do seu rival?')
nomeRival = input('> \n')
print(nomeRival, end="")
slowprint(': -Espero que esteja pronto para a Batalha Final!!!\n')
print(nomeRival, end="")
slowprint(' chama um incrivél Pikachu!!!\n')
hp = 10
hpInimigo = 10
while hp > 0 and hpInimigo > 0:

    print('\n        Escolha o ataque:\n')

    print('        1. '+principalTipo[0])
    print('        2. '+principalTipo[1])
    print('        3. '+principalTipo[2])
    print('        4. '+principalTipo[3])
    batalhaPrincipal = input('\n> ')
    if batalhaPrincipal == "1":
        slowprint(principal + ' usou '+principalTipo[0])
        hpInimigo = hpInimigo - 1
    elif batalhaPrincipal == "2":
        slowprint(principal + ' usou '+principalTipo[1])
        hpInimigo = hpInimigo - 2
    elif batalhaPrincipal == "3":
        slowprint(principal + ' usou '+principalTipo[2])
        hpInimigo = hpInimigo - 3
    elif batalhaPrincipal == "4":
        slowprint(principal + ' usou '+principalTipo[3])
        hpInimigo = hpInimigo - 4
    else:
        slowprint(principal + ' fica confuso e não ataca')

    print('\nO HP do Pikachu agora é: ', hpInimigo)
    if hpInimigo <= 0:
        break
        # batalha final - Ataques do pikachu
    else:
        slowprint('\nO Pikachu te ataca')
    ataqueInimigo = random.randint(1, 4)
    if ataqueInimigo == 1:
        slowprint('Pikachu usou Choque do Trovão')
        hp = hp - 2
    elif ataqueInimigo == 2:
        slowprint('Pikachu usou 2xChoque do Trovão')
        hp = hp - 4
    elif ataqueInimigo == 3:
        slowprint('Pikachu usou 3xChoque do Trovão')
        hp = hp - 6
    elif ataqueInimigo == 4:
        slowprint('Pikachu usou 4xChoque do Trovão')
        hp = hp - 8
    else:
        slowprint('Pikachu fica confuso e não ataca')
    print('\nO HP do seu pokémon agora é: ', hp)
if hpInimigo <= 0:

    slowprint(
        '\nVocê venceu\n')
    print("""
########     ###    ########     ###    ########  ######## ##    ##  ######     #### 
##     ##   ## ##   ##     ##   ## ##   ##     ## ##       ###   ## ##    ##    #### 
##     ##  ##   ##  ##     ##  ##   ##  ##     ## ##       ####  ## ##          #### 
########  ##     ## ########  ##     ## ########  ######   ## ## ##  ######      ##  
##        ######### ##   ##   ######### ##     ## ##       ##  ####       ##         
##        ##     ## ##    ##  ##     ## ##     ## ##       ##   ### ##    ##    #### 
##        ##     ## ##     ## ##     ## ########  ######## ##    ##  ######     #### 
            """)

elif hp <= 0:

    slowprint(
        '\nVocê foi derrotado\n')
    print("""
 ######      ###    ##     ## ########     #######  ##     ## ######## ########  
##    ##    ## ##   ###   ### ##          ##     ## ##     ## ##       ##     ## 
##         ##   ##  #### #### ##          ##     ## ##     ## ##       ##     ## 
##   #### ##     ## ## ### ## ######      ##     ## ##     ## ######   ########  
##    ##  ######### ##     ## ##          ##     ##  ##   ##  ##       ##   ##   
##    ##  ##     ## ##     ## ##          ##     ##   ## ##   ##       ##    ##  
 ######   ##     ## ##     ## ########     #######     ###    ######## ##     ## 
            """)
