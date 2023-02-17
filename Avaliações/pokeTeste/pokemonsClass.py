# Classe pokémon
class pokemonsClass:
    def __init__(self, nome, tipo, hp):
        self.nome = nome
        self.tipo = tipo
        self.hp = hp
        pass


squirtle = pokemonsClass('Squirtle', 'aquatico', '10')
charmander = pokemonsClass('Charmander', 'fogo', '10')
bulbasaur = pokemonsClass('Bulbasaur', 'grama', '10')

# Lista de ataques
aFogo = ['Rosnar',
         'Presas de Fogo',
         'Garras de Metal',
         'Explosão de Fogo']

aAgua = ['Giro Rápido',
         'Rajada de Bolhas',
         'Jato de Água',
         'Raio de Gelo']

aGrama = ['Folhas de Navalha',
          'Chicotes de Vinha',
          'Esfera de Energia',
          'Raio Solar']
