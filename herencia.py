# herencia
# consiste en crear una nueva clase a partir de una 
# o mas clases existentes
# estas enlazados unos con otros y siempre van a tener caracteristicas
# similares
#
# class nombreSubClase (nombreClaseSuperior):
# class Clase Base:
#     cuerpo de la clase base
#
# class DerivadoClase (ClaseBase):
#      cuerpo de clase derivada

class pokemon:
    pass
    def __init__(self, name, type):
        self.name = name
        self.type = type
# return lo usas para llamar los atributos en la funcion
    def description(self):
        return '{} is a pokemon type {}'.format(self.name, self.type)
class pikachu(pokemon): 
    def attack(self, attack_type):
        return '{} attack type: {}'.format(self.name, attack_type)
# para que esta clase esten enlazadas debes hacerlo con tuples (nombre de la clase arriba de ella)
class charmander(pokemon):
    def attack(self, attack_type):
        return '{} attack type: {}'.format(self.name, attack_type)

new_pokemon = pikachu('pikachu', 'electricity')
print(new_pokemon.description())
print(new_pokemon.attack('storm fire'))
# al ser hijo del hijo de la clase 'padre' (pokemon)
# pones los atributos pedidos por la clase 'padre' (name,type
# 
# a simples palabras lo que necesitas hacer es crear un objeto
# e inmediatamente trabajarlo con la clase que quieras
# obviamente poniendo los atributos que te pide la clase principal

