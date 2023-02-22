from Pokemon import inventarioJogador
from Pokemon import pokemonPrincipalRival
from Dialogos import *


class Treinador:
    def __init__(self, nome, pokemons):
        self.nome = nome
        self.pokemons = pokemons

  
    def listarPokemons():  
        printLento("Os seus Pokémons são:")
        for x in range(len(inventarioJogador)):
            print(x+1, '- ', inventarioJogador[x])

class TreinadorPrincipasl(Treinador):
    pokemons=inventarioJogador

class TreinadorRival(Treinador):
    pokemons=pokemonPrincipalRival
