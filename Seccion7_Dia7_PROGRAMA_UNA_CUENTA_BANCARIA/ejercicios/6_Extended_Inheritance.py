class Animal:
    def __init__(self, edad, color):
        self.edad = edad
        self.color = color

    def nacer(self):
        print('Este animal ha nacido...')

    def hablar(self):
        print("Este animal emite un sonido")

class Pajaro(Animal):

    def __init__(self, edad, color, altura_vuelo):
        # self.edad = edad
        # self.color = color
        super().__init__(edad, color) # Llamando al constructor de la clase padre para heredar sus atributos evitando hacerlo manualmente
        self.altura_vuelo = altura_vuelo # Agregando atributo extra a los de la clase Animal

    def hablar(self): # De mayor gerarquia con respecto al método heredado de Animal
        print('Pio')

    def volar(self, metros):
        print(f'El pajaro vuela {metros} metros')

piolin = Pajaro(3,'amarillo', 200)

piolin.hablar()

piolin.volar(100)

print(piolin.altura_vuelo)

mi_animal = Animal(5, 'gris')

mi_animal.hablar()


# Ejemplo de herencia multiple

class Padre:
    def hablar(self):
        print('Hola')

class Hijo(Padre):
    pass

class Nieto(Hijo): # La clase Nieto tendría todos los atributos y métodos tanto de Padre como de Hijo
    pass


class Madre:
    def reir(self):
        print('jaj')

class Hija(Padre,Madre): # Herencia multiple de todo lo de las clases Padre y Madre
    pass                 # en la herencia multiple hay gerarquia, si Padre y Madre
                         # ambas tienen el método reir, al instanciar una hija, el método
                         # reir que utilizará será el de la primer clase heredada, como en
                         # este caso, de Padre


# Cuando se tiene herencia multiple de muchas clases, podemos ver la gerarquía en que se heredan, 
# para saber, si hay métodos con el mismo nombre, el de cuál clase se usará
print(Hija.__mro__)

# Por esa razón debemos dar el orden correcto o lógico a las clases de las que se hereda, para evitar problemas con métodos con el mismo nombre, o para que se hereden los métodos correctos.
# Nieto(Hijo, Madre, Padre)