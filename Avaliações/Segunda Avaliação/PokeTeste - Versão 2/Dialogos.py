import os
import time

# Limpar tela
def limparTela(): return os.system('cls')

# Codigo para deixar o Texto lento
def printLento(texto, velocidadeDoTexto=0.05):
    for x in texto:
        print(x, end='', flush=True)
        time.sleep(velocidadeDoTexto)

# Logo em ASCII
def logoPokemon():
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


# Introdução
def intro():

    print("""
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓""")
    printLento("""            Bem-vindo ao emocionante mundo dos Pokémon!\n""")
    print("""┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛""")

# Dialogos

# Dialogo 01
def dialogo01():
    printLento("""
Aqui, você é um treinador de Pokémon e tem a chance de capturar,
        treinar e batalhar com seus Pokémon para se tornar
                o melhor treinador de todos!!!\n""")

    time.sleep(1)
    printLento(
        '\nVocê está em uma estrada e vê um homen sendo atacado por um Pokémon selvagem!!!\n')
    printLento(
        '\nPersonagem: O que está acontecendo?\nEsse homem está sendo atacado por um Pokémon selvagem!\n')
    printLento('\nHomem: Me ajude, por favor! Esse Pidgey selvagem ficou maluco!\n')
    printLento('\nPersonagem: O quê?! Como posso ajudá-lo?\n')
    printLento('\nHomem: Eu deixei cair minha bolsa com Pokébolas quando fui atacado.\nPegue-a e use um de meus Pokémon para afastar esse pokémon selvagem!\n')

# Dialogo 02
def dialogo02():
    printLento(
        '\nHomem: Muito obrigado!\nVocê salvou a minha vida!\nEu tenho que agradecer de alguma forma.\nAqui, eu tenho um presente para você.\nFique com esse Pokémon e estas Pokebolas como agradecimento.')
    printLento(
        '\nJogador: Obrigado! Eu sempre quis ter um pokemon!')
    printLento('\nHomem: Este é um Pokémon muito especial.\nCuide dele bem e treine-o com sabedoria.\nQuem sabe um dia você pode se tornar um mestre Pokémon!')
    printLento('\nJogador: Eu vou treiná-lo muito bem\n')
    time.sleep(1)
    printLento('\nSeguindo a estrada, você se depara com alguma opções...\n')


# Mensagens em ASCII
def gameOver():
    print("""
 ######      ###    ##     ## ########     #######  ##     ## ######## ########  
##    ##    ## ##   ###   ### ##          ##     ## ##     ## ##       ##     ## 
##         ##   ##  #### #### ##          ##     ## ##     ## ##       ##     ## 
##   #### ##     ## ## ### ## ######      ##     ## ##     ## ######   ########  
##    ##  ######### ##     ## ##          ##     ##  ##   ##  ##       ##   ##   
##    ##  ##     ## ##     ## ##          ##     ##   ## ##   ##       ##    ##  
 ######   ##     ## ##     ## ########     #######     ###    ######## ##     ## 
            """)

def parabens():
        print("""
########     ###    ########     ###    ########  ######## ##    ##  ######     #### 
##     ##   ## ##   ##     ##   ## ##   ##     ## ##       ###   ## ##    ##    #### 
##     ##  ##   ##  ##     ##  ##   ##  ##     ## ##       ####  ## ##          #### 
########  ##     ## ########  ##     ## ########  ######   ## ## ##  ######      ##  
##        ######### ##   ##   ######### ##     ## ##       ##  ####       ##         
##        ##     ## ##    ##  ##     ## ##     ## ##       ##   ### ##    ##    #### 
##        ##     ## ##     ## ##     ## ########  ######## ##    ##  ######     #### 
            """)
