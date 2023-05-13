#------------------Funciones------------------#

import csv
import json
import random
import datetime

def menu_principal(menu:list)->int:
    '''
    Brief: Muestro el menu de opciones
    Parameters: menu -> lista de opciones (el menu de opciones)
    Retorno: retorno la opcion del menu
    '''
    print("\n#---------------------------------Menu---------------------------------#\n")
    numero = -1
    booleano = False
    
    imprimir_dato(menu)

    while booleano == False:
        respuesta = input("\nIngrese una opcion: ")
        booleano = validar_entero(respuesta)
        if booleano == True:
            numero = int(respuesta)
        else:
            print("El dato ingresado no es un entero")

    return numero

def leer_csv(RUTA_CSV:str)->list:
    '''
    Brief: Lee un archivo csv, en el que tomo la informacion y lo transformo en una lista de listas
    Parameters: RUTA_CSV -> donde esta hubicado el archivo csv
    Retorno: lista_retorno -> retorno la lista de listas
    '''
    lista_diccionarios = []

    with open (RUTA_CSV, 'r', encoding='utf-8') as archivo: 
        csv_lector = csv.reader(archivo)
        for row in csv_lector:
            if len(row) != 6:
                print(f"\n¡ERROR en la fila {csv_lector.line_num}!\nEl número de columnas es incorrecto")
                continue
            else:
                diccionario = {'id': row[0], 
                'nombre': row[1], 
                'raza': row[2], 
                'poder_ataque': row[3], 
                'poder_pelea': row[4], 
                'habilidades': row[5]
            }
            lista_diccionarios.append(diccionario)

    return lista_diccionarios

def generar_csv(RUTA_BATALLA:str, fecha_actual:str, personaje_ganador:dict, personaje_perderdor:dict)->None:
    '''
    Brief: Genero un archivo csv, en donde guardo los datos pasados por parametros
    Parameters: RUTA_BATALLA -> donde se guardara el archivo csv
                fecha_actual -> fecha formateada para guardar en el archivo
                personaje_ganador -> parsonaje ganador de la batalla para guardar en el archivo
                personaje_perderdor -> parsonaje perdedor de la batalla para guardar en el archivo
    '''
    with open(RUTA_BATALLA, 'a') as archivo:
        archivo.write(": ".join(["Fecha",fecha_actual]) + '\n')
        if personaje_ganador == personaje_perderdor:
            archivo.write(" -> ".join(["Empatados",personaje_ganador['nombre']]) + '\n')
            archivo.write(" -> ".join(["Empatados",personaje_perderdor['nombre']]) + '\n')
        else:
            archivo.write(" -> ".join(["Ganador",personaje_ganador['nombre']]) + '\n')
            archivo.write(" -> ".join(["Perdedor",personaje_perderdor['nombre']]) + '\n') 

def generar_nuevo_csv(RUTA_SAIYAN:str, lista_saiyan:list)->None:
    '''
    Brief: Genero un archivo csv, en donde cargo los datos pasados por parametros
    Parameters: RUTA_SAIYAN -> donde se guardara el archivo csv
                lista_saiyan -> lista de diccionarios que mostrare en el archivo
    '''
    with open(RUTA_SAIYAN, 'w', newline='') as archivo:
        escritor = csv.writer(archivo) # acepta un objeto de archivo (file object) como argumento
        for personaje in lista_saiyan:
            fila = [personaje['id'],
                    personaje['nombre'],
                    personaje['raza'],
                    personaje['poder_ataque'],
                    personaje['poder_pelea'],
                    personaje['habilidades']]
            escritor.writerow(fila) # escribe una fila de datos en el archivo CSV

def generar_json(ruta_json:str, lista_formateada:list)->int:
    '''
    Brief: Genero un archivo json, en donde guardo los datos pasados por parametros
    Parameters: ruta_json -> donde se guardara el archivo json
                lista_formateada -> lista de personajes 
    '''
    retorno = -1

    with open(ruta_json, 'w') as archivo:
        json.dump(lista_formateada, archivo, indent=4)
        retorno = 1

    return retorno

def leer_json(ruta_json:str):
    '''
    Brief: Lee un archivo json, en el que tomo la informacion dentro del archivo y lo muestro por pantalla den forma de lista
    Parameters: ruta_json -> donde esta hubicado el archivo json
    '''
    with open(ruta_json, 'r') as archivo:
        lista = json.load(archivo)
        for personaje in lista:
            print(personaje)

def formato_ruta(ruta:str, cadena_json:str)->str:
    '''
    Brief: Armamos la ruta con un nombre formateado para ponerle al archivo json con ese mismo nombre
    Parameters: ruta -> ruta que le falta el nombre del archivo
                cadena_json -> nombre formateado del archivo que hubicaremos en la ruta
    Retorno: retorno la ruta del archivo json
    '''
    ruta_json = "".join([ruta,cadena_json])

    return ruta_json

def otorgar_poder_saiyan(lista:list, cadena:str)->list:
    '''
    Brief: Filtra los personajes de raza 'Saiyan' y los lleva a una funcion para trabajar con sus datos
    Parameters: lista -> utilizamos la lista para recorrer y buscar los Saiyans que hay en la misma
    Retorno: retorno una lista de los personajes saiyan 
    '''
    lista_saiyan = []

    if(type(lista) == list and len(lista) > 0):
        for personaje in lista:
            if cadena in personaje['raza']:
                personaje['poder_pelea'] = calcular_poder(personaje['poder_pelea'], 1.50)
                personaje['poder_ataque'] = calcular_poder(personaje['poder_ataque'], 1.70)
                personaje['habilidades'] = " |$%".join([personaje['habilidades'],"transformación nivel dios"])
                lista_saiyan.append(personaje)

    return lista_saiyan

def calcular_poder(dato:int, porcentaje_agregado:float)->list:
    '''
    Brief: Se calcula el poder del personaje 
    Parameters: dato -> poder del personaje
                porcentaje_agregado -> porcentaje con el que se multiplicara y calculara el nuevo valor
    Retorno: retorno el poder calculado
    '''
    agregado_poder = dato * porcentaje_agregado

    return agregado_poder

def pasaje_a_lista(lista:list, clave:str)->None:
    '''
    Brief: Pasaje de lista de diccionarios a lista
    Parameters: lista -> traemos a funcion la lista de diccionarios para pasar a lista las razas
                clave -> es la key que traeremos a la funcion
    '''
    if(type(lista) == list and len(lista) > 0):
        nueva_lista = cargar_lista_dato(lista, clave)

        contar_tipos(nueva_lista)
    else:
        print("Error al pasar la lista a la funcion")

def contar_tipos(nueva_lista:list)->None:
    '''
    Brief: Contador y muestra de razas
    Parameters: nueva_lista -> traemos a funcion la lista transformada y contamos los diferentes tipos de razas
    '''
    conteos_tipos = {}

    if(type(nueva_lista) == list and len(nueva_lista) > 0):
        for tipo in nueva_lista:
            tipo = tipo.capitalize()

            if tipo in conteos_tipos:
                conteos_tipos[tipo] += 1
            else:
                conteos_tipos[tipo] = 1

        print("\n#----------------Conteo_razas----------------#\n")
        for tipo, conteo in conteos_tipos.items():
            print(f"{tipo} -> {conteo}")
    else:
        print("Error al pasar la lista a la funcion")

def listar_agrupados(lista:list, clave:str)->None:
    '''
    Brief: Funcion en donde agrupo los personajes por su clave
    Parameters: lista -> lista de personajes que usaremos para reccorerla 
                clave -> clave del diccionario que se encuentra en la lista
    '''
    if(type(lista) == list and len(lista) > 0):
        lista_dato = cargar_lista_dato(lista, clave)
        lista_dato_filtrada = set(lista_dato)

        for dato in lista_dato_filtrada:
            print(dato)
            for personaje in lista:
                if dato == 'Androide-Humano':
                    if 'Androide' in personaje[clave] or 'Humano' in personaje[clave]:    
                        print(f"\t{personaje['nombre']} -- poder de ataque: {personaje['poder_ataque']}")
                elif dato == 'Saiyan-Humano':
                    if 'Humano' in personaje[clave] or 'Saiyan' in personaje[clave]:    
                        print(f"\t{personaje['nombre']} -- poder de ataque: {personaje['poder_ataque']}")             
                elif personaje[clave] == dato:
                    print(f"\t{personaje['nombre']} -- poder de ataque: {personaje['poder_ataque']}")
    else:
        print("Error al pasar la lista a la funcion")

def listado_habilidades(lista:list, clave:str)->str:
    '''
    Brief: Muestro la lista de habilidades y el usuario ingresa una habilidad de la lista
    Parameters: lista -> lista de personajes que usaremos para reccorerla y mostrarla
    Retorno: retorna la habilidad ingresada por el usuario 
    '''
    print("Habilidades:\n")

    if(type(lista) == list and len(lista) > 0):
        lista_dato = cargar_lista_dato(lista, clave) 
        lista_dato_filtrada = set(lista_dato)
        for personaje in lista_dato_filtrada:
            print(f"\t{personaje}")     
    cadena = "Ingrese una habilidad de las mostradas en la lista: "
    respuesta = ingreso_dato_usuario(lista, cadena, 'habilidades')

    return respuesta
    
def buscar_personajes_habilidad(lista:list, habilidad:str)->None:
    '''
    Brief: Busca los personajes que tengas la habilidad ingresada en la funcion 'listado_habilidades' y lo muestra
    Parameters: lista -> lista de personajes que usaremos para reccorerla y trabajar con ella
                habilidades -> habilidad ingresada por el usuario
    '''
    found = 0

    if(type(lista) == list and len(lista) > 0):
        for personaje in lista:
            if habilidad in personaje['habilidades']:
                print(f"\nNombre: {personaje['nombre']} -- Raza: {personaje['raza']}")
                promedio = calcular_promedio_fuerzas(personaje['poder_ataque'], personaje['poder_pelea'])
                print(f"Promedio entre 'poder_ataque' y 'poder_pelea': {promedio}")
                found = 1
    
    if found == 0:
        print("¡Debe ingresar una habilidad que se encuentre dentro de la lista de habilidades mostrada anteriormente!")

def buscar_personajes_cumplen(lista:list, respuesta_raza:str, respuesta_habilidad:str)->str:
    '''
    Brief: Busca los personajes que cumplan con los parametros ingresados
    Parameters: lista -> lista de personajes que usaremos para reccorerla y trabajar con ella
                respuesta_raza -> respuesta ingresada por el usuario anteriormente
                respuesta_habilidad -> respuesta ingresada por el usuario anteriormente
    Retorno: retorna una lista filtrada
    '''
    cumplen = 0
    lista_filtrada = []

    if(type(lista) == list and len(lista) > 0):
        for personaje in lista:
            if respuesta_raza in personaje['raza'] and respuesta_habilidad in personaje['habilidades']:
                lista_filtrada.append(personaje)        
                cumplen = 1
            
        if cumplen != 1:
            print("\n¡No cumplen!\n¡No existe esa combinacion de raza y habilidad!")
            lista_filtrada = "N/A"
    else:
        print("La lista no cumple con lo requerido para ser utilizada")

    return lista_filtrada

def seleccionar_personaje(lista:list)->dict:
    '''
    Brief: La funcion pide ingresar un numero entero, siendo cada numero un personaje de DBZ
    Parameters: lista -> la lista que usaremos para mostrarla y poder elegir el nombre de un personaje
    Retorno: retorno un diccionario, el personaje seleccionado
    '''
    bandera = False

    if(type(lista) == list and len(lista) > 0):
        for i, personaje in enumerate(lista):
            print(f"Índice: {i}, Nombre: {personaje['nombre']}")

        while bandera == False:
            respuesta = input("\nIngrese una opcion: ")
            bandera = validar_entero(respuesta)
            if bandera == True:
                numero = int(respuesta)
                if numero < 0 or numero > 34:
                    bandera = False
                    print("El dato ingresado tiene que estar en los valores mostrados del indice")
            else:
                print("El dato ingresado no es un entero")
    else:
        print("La lista no cumple con lo requerido para ser utilizada")
        numero = 0

    return lista[numero]

def seleccionar_personaje_random(lista:list)->dict:
    '''
    Brief: La funcion elige un personaje random de la lista de personajes
    Parameters: lista -> lista que usara para elegir un random de la misma
    Retorno: retorno el pesonaje random
    '''
    if(type(lista) == list and len(lista) > 0):
        personaje_aleatorio = random.choice(lista)

    return personaje_aleatorio

def conseguir_fecha_actual()->str:
    '''
    Brief: Funcion en donde obtenemos la fecha actual, que tenemos en nuestro ordenador
    Retorno: retorno la fecha
    '''
    fecha = datetime.datetime.now().date()
    fecha_actual = str(fecha)

    return fecha_actual

def conseguir_ganador_batalla(personaje_seleccionado:dict, personaje_random:dict)->dict:
    '''
    Brief: Funcion en donde se comparan los poderes de ataque y gana quien mayor poder tenga
    Parameters: personaje_seleccionado -> personaje seleccionado en funcion anterior
                personaje_random -> personaje random que obtuvo la maquina
    Retorno: retorno el personaje ganador de la pelea 
    '''
    if (type(personaje_seleccionado) == dict and type(personaje_random) == dict):
        if personaje_seleccionado['poder_ataque'] > personaje_random['poder_ataque']:
            personaje_ganador = personaje_seleccionado
        else:
            personaje_ganador = personaje_random
    
    print(f"El ganador es -> {personaje_ganador['nombre']}")

    return personaje_ganador

def ingreso_dato_usuario(lista:list, cadena:str, clave:str)->str:
    '''
    Biref: El usuario ingresa un dato y se recorre la lista comprobando que el dato ingresado este en la misma
    Parameters: lista -> lista que usaremos para verificar que el dato ingresado se encuentre en la misma
                cadena -> paso por parametro la pregunta que usare en el input(), asi puedo reutilizarla funcion para pedir otro ingreso de dato
                clave -> clave del diccionario
    Retorno: retorno dato ingresado
    '''
    apruebo_respuesta = False

    if(type(lista) == list and len(lista) > 0):
        while apruebo_respuesta == False:
            respuesta = input(f"\n{cadena}")
            for personaje in lista:
                if respuesta in personaje[clave]:
                    apruebo_respuesta = True
            if apruebo_respuesta != True:
                print("No se encuentra ese dato en la lista")        

    return respuesta

def formatear_lista(lista_filtrada:list, respuesta_habilidad:str)->list:
    '''
    Brief: Se arma una lista con los perosnajes que cumplen la condicion del dato pasado podr parametro 'respuesta_habilidad'
    Parameters: lista_filtrada -> lista que utilizaremos para trabajar en la funcion
                respuesta_habilidad -> respuesta ingresada por el usuario
    Retorno: retorno una lista de cadenas con un formato especifico
    '''
    lista_formateada = []

    if(type(lista_filtrada) == list and len(lista_filtrada) > 0):
        for personaje in lista_filtrada:
            nombre = personaje['nombre']
            poder_ataque = str(personaje['poder_ataque'])
            nombre_poder = " - ".join([nombre,poder_ataque])
            cadena_formateada = formatear_habilidades(personaje['habilidades'], respuesta_habilidad)
            dato_formateado = " - ".join([nombre_poder,cadena_formateada])
            lista_formateada.append(dato_formateado)
            
        return lista_formateada

def formatear_habilidades(habilidades:str, respuesta_habilidad:str)->str:
    '''
    Brief: Formateamos la cadena y la retornamos
    Parameters: habilidades -> las habilidades del personaje
                respuesta_habilidad -> respuesta ingresada por el usuario
    Retorno: retorno la cadena formateada

    '''
    habilidades = habilidades.split("|$%")
    for i in range(len(habilidades)):
        habilidades[i] = habilidades[i].strip()
    for dato in habilidades:
        if respuesta_habilidad in dato:
            habilidades.remove(dato)

    if len(habilidades) > 1:
        cadena = ", ".join(habilidades)
        cadena_formateada = cadena.replace(", "," + ")
    else:
        cadena_formateada = "".join(habilidades)

    return cadena_formateada

def formato_cadenas(respuesta_raza:str, respuesta_habilidad:str)->str:
    '''
    Brief: Formateamos la cadena y la retornamos (en este caso sera el nombre del archivo json)
    Parameters: respuesta_raza -> raza ingresada por el usuario
                respuesta_habilidad -> habilidad ingresada por el usuario
    Retorno: retorno una cadena formateada
    '''
    cadena_habilidad = respuesta_habilidad.replace(" ", "_")
    cadena_formato = "_".join([respuesta_raza,cadena_habilidad])
    cadena_json = ".".join([cadena_formato,"Json"])

    return cadena_json

def cargar_lista_dato(lista:list, clave:str)->list:
    '''
    '''
    lista_dato = []

    for diccionario in lista:
        dato = diccionario[clave]
        lista_dato.append(dato)

    return lista_dato

def calcular_promedio_fuerzas(poder_ataque:int, poder_pelea:int)->float:
    '''
    Brief: Calculo promedio de dos valores (en este caso poder_ataque y poder_pelea)
    Parameters: poder_ataque -> poder de ataque del personaje seleccionado
                poder_pelea -> poder de pelea del personaje seleccionado
    Retorno: retorno el promedio de las fuerzas
    '''
    suma_poderes = poder_pelea + poder_ataque 
    promedio = suma_poderes / 2

    return promedio

def convertir_a_entero(lista:list)->list:
    '''
    Brief: Transformo los datos (en este caso de cadena a enteros)
    Parameters: lista -> lista que recorreremos para transformar los datos de la misma
    Retorno: retorno la lista transformada
    '''
    if(type(lista) == list and len(lista) > 0):
        for diccionario in lista:
            diccionario['id'] = int(diccionario['id'])
            diccionario['poder_ataque'] = int(diccionario['poder_ataque'])
            diccionario['poder_pelea'] = int(diccionario['poder_pelea'])
    else: 
        print("\nError: Lista de héroes vacía\n")

    return lista

def imprimir_dato(dato=None)->None:
    '''
    Brief: Le paso un dato para que lo muestre por consola
    Parameters: dato -> dato de algun tipo para ser mostrado por consola de diferentes maneras
    '''
    if(type(dato) == list and len(dato) > 0):
        for opcion in dato:
            print(opcion)
    else:
        print(dato)

#--------------------------------Validaciones--------------------------------#

def validar_entero(respuesta:str)->bool:
    '''
    Brief: Funcion para validar datos enteros
    Parameters: respuesta -> recibo un input para poder validarlo en la funcion
    Return: numero -> retorno un booleano, para verificar que el dato ingresado sea entero
    '''
    booleano = False

    if respuesta.isdigit():
            booleano = True

    return booleano