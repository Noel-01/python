# For Loops

enviado = False
for n in range(4):
    print('Intento de envio...', n)    
    if enviado:
        print('Mensaje enviado')
        break
    else:
        print('No se ha podido enviar')


# Bucle While

comando = ""
while comando != "salir":
    comando = input("> ")
    print(f"el comando introducido es {comando}")