# LAMBDAS

# suma sin usar lambda
def sumar(x,y):
    return x + y

# suma usando lambda
sumaLambda = lambda x, y : x + y

print(sumar(4,2))
print(sumaLambda(4,2))


lista = [1,2,3,4,5,6,7,8,9,10]
lista_filtrada = filter(lambda numero: numero %2 == 0, lista)
pares = list(lista_filtrada)
print(pares)

# MAP
productos2 = [
    ('producto1', 10),
    ('producto2', 20),
    ('producto3', 30),
    ('producto4', 40)
]

# sin map
for procuto in productos2:
    print(procuto[0])

# con map
precios = list(map(lambda producto: producto[1], productos2))
print(precios)


# Reducir aun mas el Lambda y el Filter y hacer COMPRIMIDOS
productos3 = [
    ('producto1', 100),
    ('producto2', 10),
    ('producto3', 12),
    ('producto4', 130)
]

# filtrados
productos_filtrados = list(filter(lambda item: item[1] >= 100, productos3))
print('productos filtrados ', productos_filtrados)

# mapeados
productos_mapeados = list(map(lambda producto: producto[1], productos3))
print('productos mapeados ', productos_mapeados)

# Comprimidos filtrados
prod_filtrados_comprimidos = [item for item in productos3 if item[1] >= 100] # el primer item es lo que devuelve, primero hacer el for luego el if y lo devuelve en el primer item
print(prod_filtrados_comprimidos)

# Comprimidos mapeados
prod_mapeados_comprimidos = [item[1] for item in productos3] # hace el for y lo guarda en el item
print(prod_mapeados_comprimidos)