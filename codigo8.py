# Arrays
# Ver la pagina docs.python.org/3/library/array.html#module-array, aquí se pueden ver los tipo de codigo con el que se quiere crear el Array

from array import array

numeros = array('i', [1,2,3,4,5,6,7,8]) # como tiene una 'i' es de tipo int


# Diccionarios
personas = {
    'nombre': 'Noel',
    'edad': 32
}

personas['nombre'] = 'Josse'
print(personas)
print(personas['nombre'])

# se puede asignar una nueva propiedad
personas['altura'] = 2
print(personas)

# comprobar si existe una propiedad
if 'propiedad' in personas:
    print(personas['propiedad'])


# Usando Getters
print(personas.get('nombre'))

print(personas.get('propiedad')) # Como esto no existe devuelve un None

print(personas.get('propiedad', 'esta persona no tiene propiedad')) # Como se que no tiene la propiedad le puedo añadir un mensaje de error


# borrar una propiedad
del personas['edad']
print(personas)