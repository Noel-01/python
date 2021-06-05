# SCOPE el alcance de las variables.

mensaje = 'hola'

def mostrar():
    mensaje = 'adios' # Esto no es válido puesto que python no considera global a la variable mensaje y no la puede modificar

mostrar()
print(mensaje) #Imprime hola


# Elevar el SCOPE de las variables usando 'global'

otroMensaje = 'otroHola'

def mostrar():
    global otroMensaje
    otroMensaje = 'otroAdios' # Esto no es válido puesto que python no considera global a la variable mensaje y no la puede modificar

mostrar()
print(otroMensaje) #Imprime hola
