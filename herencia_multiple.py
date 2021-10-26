# herencia multiple:
# la herencia multiple see refiere a la posibilidad de crear una clase a partir de multiples clases superiores
#
#
# Estructura herencia multiple: 
# class base_uno:
#          pass
# class base_dos:
#          pass
# class derivadosMultiple (base_uno, base_dos):
#             pass
#
#
# en la herencia multinivel, las caracteristicas de la clase base  y la clase derivada se heredan en la nueva clase derivada
#
#
# Estructura herencia multinivel: 
# class base:
#          pass
# class derivado-uno(base):
#          pass
# class derivado-dos(derivado-uno):
#             pass


class phone:
    def __init__(self):
        pass
    def call(self):
        print('calling...')
    def hold(self):
        print('hold...')

class camera:
    def __init__(self):
        pass
    def photography(self):
        print('taking photograph...')

class play:
    def __init__(self):
        pass
    def playing(self):
        print('playing music...')
    def playing_video(self):
        print('playing video...')

class smartphone(phone, camera, play):
    def __del__(self):
        print("phone off")
#
# usamos __del__() escencialmente para limpiar los recursos, en python los objetos y clases no utlizadas 
# se eliminan automaticamente cuando ya no se le usa.
#
movil = smartphone()
print(movil.photography())