# LISTAS

letras = ['a', 12, True, 'c', ['Noel', 'Juan']]
print(letras)

# Concatenar listas
letras_dos = ['a', 'b', 14] + letras
print(letras_dos)

# Funcion List, si el valor es iterable lo serpara
nombre = list('Noel')
print(nombre)

# Aceso a listas
datos = [1,2,3,4,5,6,7]
print(datos[2]) # impreme la posición 2 que es el numero 3
datos[2] = 'Noel'
print(datos)

print('El tamanio de las lista es: ', datos[-1])

# Dar la vuelta a una lista
print(datos[::-1])

# Desempaquetar una lista
lista = [1, 2, 3]
numero1, numero2, numero3 = lista
print(numero1, numero2, numero3)

# Con *otros se puede almacenar el resto de valores que hay en la lista
numero, *otros = lista
print(numero, otros)

# Recorrer listas
lista1 = [1,2,3,4,5]

for numero in lista1:
    print(numero)

# Sacar la tupla, posición y valor de la lista
for numero in enumerate(lista1):
    print(numero)

# Mas elegante xD
for index, numero in enumerate(lista1):
    print(index, numero)


# Añadir o eliminar elementos en las listas
lista2 = [1,2,3,4,5]

lista2.append(6) # Añade
print(lista2)

lista2.insert(2, 2.5) # El primer parametro es la posicion donde se inserta, pero sin sustituir la que ya hay.
print(lista2)

lista2.remove(2) # NO es la POSICION, es el numeo que se encuentra dentro. Un error que tiene es ques si existe varios numeros 2, solo elimina el primero.
print(lista2)

lista2.pop() # Elimina el ulitimo elemento de la lista
print(lista2)

# Metodos de listas
lista3 = [1,2,3,4,5]
numero_veces = lista3.count(3) # Devulve el numero de veces que está el numero 3 en la lista. En este caso 1 vez.
print(numero_veces)

indice = lista3.index(4) # Devuelve la posición en el que se encuentra el varlo 4
print(indice)

indice = lista3.index(4, 2) # Busaca el numero 4 partiendo de la posición 2 y devuelve la posición del numero 4
print(indice)

# Ordenar listas
lista4 = [2 ,9 ,4 ,7 ,6, 3]

print(sorted(lista4)) # Esta es una forma

lista4.sort() # Esta es otra forma
print(lista4)


# Ordenar listas con mas de un valor
productos = [
    ('producto1', 20),
    ('producto2', 40),
    ('producto3', 5)
]

def ordenar_items(item):
    return item[1] # Esto hacer referncia a lo que yo quireo que se la clave (key) en el este caso la posición 1 que son los valores 20, 40 y 5

productos.sort(key=ordenar_items)
print(productos)

