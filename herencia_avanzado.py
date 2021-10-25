#
# ingresar datos por consola, cool
# limitar la cantidad de valores que introduces por teclado
# con este bucle solo imprime el numero que el usuario indique
# [0 for i in range(number)] (es un bucle)
# 'self' nos ayuda a llamar al metodo
#
#
class calc:
    def __init__(self, number):
        self.number = number
        self.data = [0 for i in range(number)]
    
    def set_data(self):
        self.data = [int(input('set data '+str(i+1)+ '= ')) for i in range(self.number)]

class basic_op(calc):
    def __init__(self):
            calc.__init__(self, 2)

    def add(self):
        a, b, = self.data
        s = a + b
        print(s)

    def substract(self):
        a, b, = self.data
        r = a - b
        print(r)

class raiz(calc):
    def __init__(self):
            calc.__init__(self, 1)
    
    def cuadrada(self):
        import math
        a, = self.data
        print('result', math.sqrt(a))

example = basic_op()
print(example.set_data())
print(example.add())

example = raiz()
print(example.set_data())
print(example.cuadrada())

object = basic_op()

# isinstance lo que hace es verificar la herencia con 'True' or 'False'
isinstance(object, basic_op)
print(isinstance(object,basic_op))
# issubclass lo que hace es verificar la herencia via subclase con 'True' or 'False'
issubclass(calc, basic_op)
print(issubclass(calc, basic_op))
