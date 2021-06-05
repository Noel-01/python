#Operadores de comparación.

# mayor
print(4>1)

# menor
print(4<1)

# mayor o igual
print(4>=1)

# menor o igual
print(4<=1)

# igualdad
print(4==1)

# negación
print(4!=1)

verdad = True
print(not verdad)

falso = False
print(not falso)


# Condicional IF

edad = 20
if edad > 18:
    print('Eres mayor de edad')
elif edad <= 17:
    print('Eres menor de edad')
else:
    print('No tienes edad, eres un vampiro')


mensaje = 'Mayor de edad' if edad >= 18 else "menor de edad"
print(mensaje)


# Operadores Lógicos

x = True
y = True

# and las dos vedaderas para se vedadero
if x == y and x > y:
    print('AND es true')

# una de ellas tiene que ser vedadera para ser vedadero
if x == y or x > y:
    print('OR es true')


# Concatenación de operaciones de comparación
edad2 = 18
# if edad >= 18 and edad < 65: // esto es lo mismo que la siguiente linea
if 18 >= edad2 < 65:
    print('estas en edad de trabajar')
