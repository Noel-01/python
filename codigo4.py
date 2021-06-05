# FUNCIONES

def nombre_funcion():
    print('Hola desde dentro de la funcion')

print('Hola desde fuera de la funcion')

# Con llamarla ya se muestra por pantall
nombre_funcion()


# MAS FUNCIONES CON PARAMETROS

def saludar(nombre):
    print('Hola me llamo', nombre)

saludar('Noel')

# Tipos de funciones

# Las que realizan acciones
print('hola')

# Las que devuelven un dato
def sumar(n1, n2):
    return n1 + n2

print(sumar(2,5))    

# Tambien se pude hacer esto pero no es lo nomal
print(sumar(1, n2=5))

# o tambien
variableSumar = sumar(4, n2=5)
print(variableSumar)


# PARAMETROS XARGS o argumentos X, se usa el * y se pasan como si fuese una lista de algo, int, strings, etc...

def sumar_x_args(*numeros):
    total = 0
    for numero in numeros:
        total += numero
    return total

print(sumar_x_args(1,3,2,5,2,1))    

# PARAMETROS PARA DICCIONARIOS

def mostrar_usuario(**usuario):
    print(usuario['nombre']) # Con esto le dices que dentro de usuario va a existir un parametro que se llame nombre y que te lo imprima

print(mostrar_usuario(id=1, nombre="Noel"))
