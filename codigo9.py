# Clases y Objetos

# Clase básica
from array import array


class Persona:

    # constructor
    def __init__(self, nombre, apellido): # self es lo mismo que this en java
        self.nombre = nombre
        self.apellido = apellido

    def caminar(self):
        print(f'{self.nombre} esta caminando')



noel = Persona('Noel', 'Apellido')
noel.caminar()

victoria = Persona('Victoria', 'Mas')
victoria.caminar()


class Punto:

    c = 14 # propiedad comun para todos los puntos

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def mostrar_puntos(self):
        print(f'{self.a}, {self.b}')

    # Como un toString()
    def __str__(self):
        return f'este objeto tiene los valores a={self.a}, b={self.b} y c={self.c}'



punto_a = Punto(1,2)
punto_b = Punto(3,4)

print(punto_a.a)
print(punto_b.a)

print(punto_a.c)
print(punto_b.c)

print(punto_a)
