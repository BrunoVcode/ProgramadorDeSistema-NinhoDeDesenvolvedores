class pokemonsClass:
    def __init__(self, nome, tipo, hp, ataques):
        self.nome = nome
        self.tipo = tipo
        self.hp = hp
        self.ataques = ataques
        pass


squirtle = pokemonsClass('Squirtle', 'aquatico', '10', 'Jato de Água')
charmander = pokemonsClass('Charmander', 'fogo', '10', 'Explosão de Fogo')
bulbasaur = pokemonsClass('Bulbasaur', 'grama', '10', 'Chicote de vinhas')
