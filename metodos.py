# metodos
# un metodo es una funcion en si
# pero esta dentrode una class
# basicamente es una funcion pero cuando esta dentro de una class
# se le dice metodo
# "self" hace una referencia a un determinado objeto que no haz creado
# class nombre de la clase:
#     def nombre del metodo(self):
#                          self.nombre de la variable = valor

class Matematica: 
    def suma(self):
        self.n1 = 2
        self.n2 = 3

sumar = Matematica()
sumar.suma()
print(sumar.n2 + sumar.n1)

# otra forma
#'_init_' (iniar)

class ropa: 
    def __init__(self):
        self.brand = "Louis Vuitton"
        self.size = 'M'
        self.color = 'Black'

shirt = ropa()
print(shirt.brand)
print(shirt.size)


class calc:
    def __init__(self, n1, n2):
        self.add = n1 + n2
        self.substract = n1 - n2
        self.multiplication = n1 * n2

operation = calc(2, 3)
print(operation.substract)
print(operation.multiplication)
print(operation.add)



