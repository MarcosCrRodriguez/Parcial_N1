'''
# Lista de diccionarios con una clave que contiene otra lista
lista_diccionarios = [
    {'nombre': 'Juan', 'edades': [25, 30, 35]},
    {'nombre': 'Maria', 'edades': [28, 33]},
    {'nombre': 'Pedro', 'edades': [20, 27, 32]}
]

# Recorrer la lista de diccionarios
for diccionario in lista_diccionarios:
    # Imprimir el nombre de la persona
    print(diccionario['nombre'] + ':')
    
    # Recorrer la lista de edades dentro del diccionario
    for edad in diccionario['edades']:
        # Imprimir cada edad
        print(edad)


# Lista de diccionarios con una clave que contiene otra lista
lista_diccionarios = [
    {'nombre': 'Juan', 'edades': [25, 30, 35, 20]},
    {'nombre': 'Maria', 'edades': [28, 33, 30, 25]},
    {'nombre': 'Pedro', 'edades': [20, 27, 32, 35]}
]

# Nueva lista vacía para acumular los valores
lista_edades = []

# Recorrer la lista de diccionarios
for diccionario in lista_diccionarios:
    # Extender la nueva lista con la lista de edades dentro del diccionario
    lista_edades.extend(diccionario['edades'])

# Imprimir la nueva lista con todos los valores
lista_edades = set(lista_edades)
lista_nueva = []
for dato in lista_edades:
    lista_nueva.append(dato)
print(lista_nueva)
'''

# Lista de diccionarios con una clave que contiene otra lista
lista_diccionarios = [
    {'nombre': 'Juan', 'edades': [25, 30, 35]},
    {'nombre': 'Maria', 'edades': [28, 33]},
    {'nombre': 'Pedro', 'edades': [20, 27, 32]}
]

# Dato a buscar
dato = 30

# Recorrer la lista de diccionarios
for diccionario in lista_diccionarios:
    # Verificar si el dato está en la lista de edades dentro del diccionario
    if dato in diccionario['edades']:
        # Imprimir el nombre de la persona y el dato que se encontró
        print(f"{diccionario['nombre']} tiene {dato} en su lista de edades")

'''
# Lista de diccionarios con una clave que contiene otra lista
lista_diccionarios = [
    {'nombre': 'Juan', 'edades': [25, 30, 35, 28]},
    {'nombre': 'Maria', 'edades': [28, 33, 22, 20]},
    {'nombre': 'Pedro', 'edades': [20, 27, 32, 35, 26]}
]

# Conjunto para llevar un registro de los elementos ya impresos
elementos_impresos = set()

# Recorrer la lista de diccionarios
for diccionario in lista_diccionarios:
    # Imprimir el nombre del diccionario
    print(diccionario['nombre'])
    
    # Recorrer la lista de edades dentro del diccionario
    for edad in diccionario['edades']:
        # Imprimir la edad solo si aún no ha sido impresa
        if edad not in elementos_impresos:
            print(edad)
            # Agregar la edad al conjunto de elementos ya impresos
            elementos_impresos.add(edad)
'''