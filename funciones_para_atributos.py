# funciones para atributos 
# nos sirven bastante para agilizar el proceso de crear objetos
# con atributos que estan dentro de una clase
# siempre recuerda los '()' dude

class person:
    age = 18
    name = 'roswart'

programmer = person()
print(programmer.name)
print('his age:', programmer.age)

# getattr() (obtiene el atributo de manera directa)
print('his age:', getattr(programmer, 'age'))

#  hasattr() (con esto sabemos si algo es 'True' or 'False'
#  si realmente pertenece o no pertenece)
print('does the programmer has an age?', hasattr(programmer, 'age')) 

# setattr() (esta funcion funciona para hacer cambios)
print(programmer.name)
setattr(programmer, 'name', 'oorigamy')
print(programmer.name)

# delattr() (elimina un atributo dicho por el usuario del objeto)
delattr(programmer, 'age')
print(programmer.age)