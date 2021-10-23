
# clase y objeto
# una class es algo a lo que le pones un nombre que 
# almacena 'objetos' del mismo caracter
# objeto es la "variable" que esta dentro de la class
# crear una clase (class 'Nombre':)
# siempre terminar con ':'
class Auto:
    marca = ""
    modelo = 2004
    placa = ""
# los elemntos dentro de la clase se representan
# de la misma forma base que las variables (eje arriba) 

# '()' para que haga referencia a que "taxi" es de class Auto
taxi = Auto()
print(taxi.modelo)
# para print algo especifico en tu variable parte de tu clase
# llamas print("variable.objeto")


#clases y objetos

class Persona:
    doctor = "felix"

# para llamar una clase debes llamarla de la forma abajo
#  "class_name.objeto"
print(Persona.doctor)

# el class y el print para poder llamando tienen que estar
# a la misma altura
class jugadores_A:
    j1 = "messi"
    j2 = 'c.ronaldo'

print(jugadores_A.j2)

class jugadores_B:
    j3 = 'neymar'
    j1 = 'marcelo'

print(jugadores_B.j1)
# dos objetos pueden tener el mismo nombre 
# si estan almacenados en diferentes clases
# solo llamas 'print(clase.objeto)' especificas cual y te lo imprimira
# si estan en la misma clase, python va a imprimir el que esta en la ultima linea de codigo

class equipo:
    e2 = 'barcelona'
    e3 = 'madrid'

print(equipo.e3)

# no necesariamente los objetos tienen que estar definidos en la clase si o si
# si no que puedes crear la clase y definir los objetos luego en el codigo
# usando "objeto.atributos = valor"
class nombre:
    pass

roswart = nombre()
alex = nombre()

roswart.edad = 18 
roswart.estatura = 1.83
roswart.sexo = 'hombre'
roswart.pais = 'DR'

# no necesariamente tienes que usar los mismos atributos para cada objeto
alex.comida_favorita = 'pizza'
alex.trabajo = 'doctor'
alex.pronombres = 'he/him'
alex.hijos = 0

print(roswart.edad)
print(alex.hijos)
print(roswart.pais)

