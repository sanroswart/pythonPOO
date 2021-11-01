# f-string 
# son utilizados por ser muy rapidos 
# (format %)
# siempre usar '% s' en el string en la parte donde quieres que este tu 
# f-string, y luego ponerle 
# '%' al final seguido de los nombres de las variables del string
#str.format

curso = 'python'
print("how to use % s"%curso)

nombre = 'roswart'
edad = 18
print("hello i'm % s and i'm % s y/o"%(nombre, edad))

print("i'm {} and i'm {} y/o ".format(nombre, edad))

print(f'im {nombre} and im {edad} y/o')

class student:
    def __init__(self, name, last_name, age):
        self.name = name 
        self.last_name = last_name
        self.age = age

    def __repr__(self):
        return f"{self.name} {self.last_name} {self.age}"
new_student= student('roswart', 'stev', 18)
print(f'{new_student !r}')
# generalmente __str__() se usa para retornar resultados inmediatamente 
# es la representacion informal de una cadena o un objeto

# __repr__() lo opuesto a __str__() (es una representacion formal)
# !r se usa con repr
