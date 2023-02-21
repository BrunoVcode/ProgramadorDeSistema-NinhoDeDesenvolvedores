from Pokemon import *
from Treinador import *
from Dialogos import *




# Limpar a tela
limparTela
# Logo em ASCII
logoPokemon()

# Introdução
intro()
dialogo01()  # Os dialogos estão em um aquivo separado.


#Escolha 01 - Salvar desconhecido(neste trecho, foi utilizado
#o comando de repetição “while True:”, fazendo com que o código
#seja repetido até que o jogador escolha a opção “certa” ou saia do jogo.

while True:
    print("\nSelecione uma opção:")
    print("1. Fugir")  # game over.
    # Essa opção leva a um loop que retorna ao menu.
    print("2. Falar novamente com o homem")
    # opção correta. que dá prosseguimento ao jogo.
    print("3. Pegar uma das pokebolas no chão")
    print("4. Sair do jogo")

    escolha = input("> ")

    if escolha == "1":
        printLento('\nVocê tenta fugir, mas cai e bate a cabeça em uma pedra. \n')
        gameOver()
        exit()

    elif escolha == "2":
        printLento('\nHomem: Me ajude, por favor!\n')
    elif escolha == "3":
        printLento("\nQual Pokebola você escolhe?\n")
        break
    elif escolha == "4":
        printLento("Obrigado por jogar!")
        exit()
    else:
        print("Opção inválida. Por favor, escolha um número de 1 a 4.")

# Escolha 02 - Escolher pokémon inicial (Dependendo da Pokébola escolhida
#o jogador recebe um pokémon diferente)



while True:
    print("1. Pegar a pokebola azul")  # Squirtle
    print("2. Pegar a pokebola vermelha")  # Charmander
    print("3. Pegar a pokebola verde")  # Bulbasaur
    print("4. Sair do jogo")

    opcao = input("> ")
    if opcao == "1":
        printLento('\nVocê pega a pokebola azul. \nE dela sai um Squirtle!!!\n')
        inventarioJogador[0] = squirtle
        pokemonPrincipal[0] = squirtle
        break
    elif opcao == "2":
        printLento(
            '\nVocê pega a pokebola vermelha. \nE dela sai um Charmander!!!\n')
        inventarioJogador[0] = charmander
        pokemonPrincipal[0] = charmander
        break
    elif opcao == "3":
        printLento('\nVocê pega a pokebola verde. \nE dela sai um Bulbasaur!!!\n')
        inventarioJogador[0] = bulbasaur
        pokemonPrincipal[0] = bulbasaur
        break
    elif opcao == "4":
        print("Obrigado por jogar!")
        exit()
    else:
        print("Opção inválida. Por favor, escolha um número de 1 a 4.")

# Batalha 01 - Pokémon Selvagem

# A progamação da batalha está em um arquivo externo.
venceu = Pokemon.batalha(pokemonPrincipal[0], pidgey)
if venceu==True:
    dialogo02()
else:
    printLento('\nVocê foi derrotado. \n')
    gameOver()
    exit()    

# Dialogo 02




# Escolha 03 - Jornada do héroi

while True:
    print('')
    printLento("Escolha o que quer fazer:")
    print('')
    # Aqui é possivel procurar batalhas aleatoriamente.
    print("1. Procurar Batalhas")
    # verifica e escolhe o Pokémon principal.
    print("2. Verificar seus Pokémons")
    # Final do jogo(ainda não implementado)
    print("3. Seguir em frente e enfrentar seu Rival")
    print("4. Sair do jogo")

# Neste trecho, tive dificuldades em fazer o codigo funcionar no aquivo externo.
    escolha03 = input("> ")
    if escolha03 == "1":
        printLento('\nVocê Procura Pokémons Selvagens nos aredores...')
        print('')
        Pokemon.escolherPokemonAleatorio()
        venceu = Pokemon.batalha(pokemonPrincipal[0], pokemonAleatorioLista[0])
        if venceu==True:
            Pokemon.capturarPokemon()
        else:
            print('')

    elif escolha03 == "2":
        printLento(
            '\nVocê verifica suas pokebolas.')
        print('')
        Pokemon.escolherPokemon()

    elif escolha03 == "3":
        printLento('\nVocê está confiante que pode derrotar seu Rival!!!\n')
        print('')
        venceu = Pokemon.batalha(pokemonPrincipal[0], pokemonPrincipalRival[0])
        if venceu==True:
            limparTela()
            printLento('\nVocê finalizou o jogo!!!\n')
            parabens()
            break

        else:
            printLento('\nVocê foi derrotado. \n')
            gameOver()
            exit()


    elif escolha03 == "4":
        print("Obrigado por jogar!")
        exit()
    else:
        print("Opção inválida. Por favor, escolha um número de 1 a 4.")


