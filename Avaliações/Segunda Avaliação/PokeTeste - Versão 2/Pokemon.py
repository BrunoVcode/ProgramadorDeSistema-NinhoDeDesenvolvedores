import random
from Dialogos import *

class Pokemon:
    def __init__(self, nome, tipo, vida, ataques):
        self.nome = nome
        self.tipo = tipo
        self.vida = vida
        self.ataques = ataques
        self.vidaInicial = vida

    def restaurarVida(self):  
        self.vida = self.vidaInicial

    def mostrarNome(self):
        printLento(f"{self.nome}")

    def mostrarTipo(self):
        printLento(f"{self.tipo}")

    def mostrarNomeTipo(self):
        printLento(f"{self.nome} - {self.tipo} -")

    def escolherPokemon():
        print("Selecione um dos seguintes Pokemons:")
        for x in range(len(inventarioJogador)):
            print(x+1, "-", inventarioJogador[x].nome)

        print("Digite o número correspondente ao Pokemon escolhido: ")
        print('> ',end="")
        escolha = int(input())

        if escolha < 1 or escolha > len(inventarioJogador):
            print("Escolha inválida.")
        else:
            pokemonPrincipal[0] = inventarioJogador[escolha-1]
            print("Você escolheu o Pokemon", pokemonPrincipal[0].nome)
            return pokemonPrincipal[0]
     
    def escolherPokemonAleatorio():
        while True:
            pokemonAleatorio = random.choice(listaPokemon)
            if pokemonAleatorio != pokemonPrincipal[0]:
                pokemonAleatorioLista[0] = pokemonAleatorio
                break
            else:
                print('')

    def capturarPokemon():
        printLento(f'Você quer capturar o {pokemonAleatorioLista[0].nome}?')
        print('')
        print("1. Sim")
        print("2. Não")
        escolhaCapturar = input("> ")
        if escolhaCapturar == "1":
            inventarioJogador.append(pokemonAleatorioLista[0])
            printLento(f"Parabéns! Você capturou {pokemonAleatorioLista[0].nome}!")
            print('')
        else:
            print('')

    def batalha(jogador, oponente):
        print('')
        venceu = False
        printLento("Batalha iniciada!")
        print('')
        printLento(
            f"{jogador.nome} ({jogador.tipo}) vs. {oponente.nome} ({oponente.tipo})")
        print('')
        while jogador.vida > 0 and oponente.vida > 0:
            Pokemon.turnoJogador(jogador, oponente)
            if oponente.vida <= 0:
                break
            Pokemon.turnoOponente(oponente, jogador)
        if jogador.vida <= 0:
            print('\n')
            printLento(f"{jogador.nome} foi derrotado!")
            print('\n')
            jogador.restaurarVida()
            oponente.restaurarVida()
            printLento("Fim da batalha.")
            print('')
            
        else:
            print('\n')
            printLento(f"{oponente.nome} foi derrotado!")
            print('')
            printLento('Você Venceu!!!')
            print('\n')
            venceu = True
            jogador.restaurarVida()
            oponente.restaurarVida()
            printLento("Fim da batalha.")
            print('')
            return venceu
        print('')


    def turnoJogador(jogador, oponente):
        print('')
        printLento("---------- Seu Turno ----------")
        print('')
        printLento("Escolha um ataque:")
        print('\n')
        for i, ataque in enumerate(jogador.ataques.keys()):
            print(f"{i+1}. {ataque}")
        escolha = int(input('> ')) - 1
        if escolha >= 2:
            print('O Pokémon fica confuso, e não ataca')

        else:
            nomeAtaque = list(jogador.ataques.keys())[escolha]
            poderAtaque = list(jogador.ataques.values())[escolha]
            printLento(f"{jogador.nome} usou {nomeAtaque}!")
            print('\n')
            dano = poderAtaque
            oponente.vida -= dano
            printLento(f"{oponente.nome} perdeu {dano:.0f} pontos de vida.")
            print('')
            printLento(
                f"{oponente.nome} tem {oponente.vida:.0f} pontos de vida.")
            print('')


    def turnoOponente(oponente, jogador):
        print('')
        printLento('------- Turno do oponente -------')
        print('')
        printLento(f"{oponente.nome} atacou!")
        print('')
        nomeAtaque, poderAtaque = random.choice(
            list(oponente.ataques.items()))
        printLento(f"{oponente.nome} usou {nomeAtaque}!")
        print('\n')
        dano = poderAtaque
        jogador.vida -= dano
        printLento(f"{jogador.nome} perdeu {dano:.0f} pontos de vida.")
        print('')
        printLento(f"{jogador.nome} tem {jogador.vida:.0f} pontos de vida.")
        print('')







charmander = Pokemon("Charmander", "Fogo", 10, {"Brasas": 2, "Chama": 4})
squirtle = Pokemon("Squirtle", "Água", 10, {"Bolhas": 2, "Jato de Água": 4})
bulbasaur = Pokemon("Bulbasaur", "Planta", 10, {
                    "Chicote de Vinhas": 2, "Raio Solar": 4})
butterfree = Pokemon("Butterfree", "Inseto", 10, {
                     "Tiro de Seda": 2, "Vento Prateado": 4})
pidgey = Pokemon("Pidgey", "Voador", 10, {"Bicada": 2, "Golpe Aéreo": 4})
pikachu = Pokemon("Pikachu", "Elétrico", 10, {
                  "Investida Trovão": 4, "Choque do Trovão": 8})

listaPokemon = [charmander, squirtle, bulbasaur, butterfree, pidgey]
pokemonPrincipalRival = [pikachu]
pokemonPrincipal = [None]
inventarioJogador = [None]
pokemonAleatorioLista = [None]
