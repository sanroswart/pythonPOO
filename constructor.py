# constructor 
# '__init__()' (normalmente lo usamos para inicializar todo tipo de variable)
# recuerden que un metodo siempre debe tener un (self)
# las '{}' son para cumplir la funcion del .format() con los objetos
# espacios en python son muy importantes

class persona:
    pass
    def __init__(self, name, year):
        self.name = name
        self.year = year
    def description(self):
        return ' {} was born in {}'.format(self.name, self.year)
    def comment(self, phrase):
        return ' {} says {}'.format(self.name, phrase)

doc = persona('Roswart', 2002)
print(doc.description())
print(doc.comment('i love u, baby Lau <3'))


# modificar un atributo
# esto quiere decir que puedes cambiar el valor
# de los atributos en funcion a un comportamiento

class email: 
    def __init__(self) -> None:
        
        self.sent = False
    def mail_sent(self):
        self.sent = True

my_email = email()
print(my_email.sent)

# para llamar un objeto de mismo nombre tienes que ser un poco mas especifico
# en este caso para llamar el sent = true deberias de especificar primero
# a que quieres que se conecte tu variable con un '.' y luego corre el atributo
# just like i did here below
my_email.mail_sent()
print(my_email.sent)

