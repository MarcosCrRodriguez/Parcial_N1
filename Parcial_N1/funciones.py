#------------------Funciones------------------#

import re
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

def limpiar_dato(lista:list, clave:str)->list:
    '''
    Brief: Funcion que transforma una cadena en una lista, sacando los espacios vacios de los datos de la nueva lista
    Parameters: lista -> lista que utilizazremos para recorrerla y transformar los datos
                clave -> valor de la clave que transformaremos los datos
    Retorno: retorno de la lista modificada
    '''
    for personaje in lista:
        personaje[clave] = personaje[clave].split("|$%")
        for i in range(len(personaje[clave])):
            dato = personaje[clave][i]
            dato_strip = dato.strip()
            personaje[clave][i] = dato_strip
    
    return lista

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
                personaje['habilidades'].append("transformación nivel dios")
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

        print("\n#----------------Agrupación_razas----------------#\n")

        for dato in lista_dato_filtrada:
            print(dato)
            for personaje in lista:            
                if personaje[clave] in dato:
                    print(f"\t{personaje['nombre']} -- poder de ataque: {personaje['poder_ataque']}")
    else:
        print("Error al pasar la lista a la funcion")

def ingresar_habilidad(lista:list, cadena:str, clave:str)->str:
    '''
    Brief: Ingreso de dato del usuario
    Parameters: lista -> muestro y recorro la lista verificando que el dato ingresado este dentro de la misma       
                cadena -> esta cadena es la pregunta que le haremos al usuario para ingresar un dato
                clave -> clave del diccionario que necesitaremos para verificar si se encuentra el dato ingresado en ella
    Retorno: retorna el dato ingreasdo por el usuario    
    '''
    encontrado = 0
    apruebo_respuesta = False
    print("\n#----------------Habilidades----------------#\n")
    
    if(type(lista) == list and len(lista) > 0):
        while apruebo_respuesta == False:
            mostrar_lista_dict_lista(lista, clave)
            respuesta = input(f"\n{cadena}")
            for diccionario in lista:
                for dato in diccionario[clave]:
                    if respuesta == dato:
                        apruebo_respuesta = True  
                        encontrado = 1
            if encontrado != 1:
                print("No se ha encontrado el dato ingresado en la lista") 
    else:
        print("La lista no cumple con lo requerido para ser utilizada")

    return respuesta

def buscar_personajes_habilidad(lista:list, dato_ingresado:str, clave:str)->None:
    '''
    Brief: Busca los personajes que tengas la habilidad ingresada en la funcion 'listado_habilidades' y lo muestra
    Parameters: lista -> lista de personajes que usaremos para reccorerla y trabajar con ella
                dato -> habilidad ingresada por el usuario
                clave -> valor de clave que necesitamos encontrar
    '''
    if(type(lista) == list and len(lista) > 0):
        for diccionario in lista:
            for dato in diccionario[clave]:
                if dato_ingresado in dato:
                    mostrar_personaje(diccionario['nombre'], diccionario['raza'], diccionario['poder_ataque'], diccionario['poder_pelea'])
    else:
        print("La lista no cumple con lo requerido para ser utilizada")

def mostrar_lista_dict_lista(lista:list, clave:str)->None:
    '''
    Brief: Muestro la lista por consola
    Parameters: lista -> lista que recorreremos 
                clave -> valor de clave que mostraremos
    '''
    elementos_impresos = set()

    if(type(lista) == list and len(lista) > 0):
        for diccionario in lista:
            for dato in diccionario[clave]:
                if dato not in elementos_impresos:
                    print(dato)
                    elementos_impresos.add(dato)

def mostrar_personaje(nombre:str, raza:str, poder_ataque:int, poder_pelea:int)->None:
    '''
    Brief: Muestro un personaje con sus datos
    Parameters: nombre -> nombre de personaje
                raza -> raza del personaje
                poder_ataque -> poder de ataque del personaje
                poder_pelea -> poder de pelea del personaje
    '''
    print(f"\nNombre: {nombre} -- Raza: {raza}")
    promedio = calcular_promedio_fuerzas(poder_ataque, poder_pelea)
    print(f"Promedio entre 'poder_ataque' y 'poder_pelea': {promedio}")    

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
            if respuesta_raza in personaje['raza']:
                for habilidad in personaje['habilidades']:
                    if respuesta_habilidad == habilidad: 
                        lista_filtrada.append(personaje)        
                        cumplen = 1
        if cumplen != 1:
            print("\n¡No cumplen!\n¡No existe esa combinacion de raza y habilidad!")
            lista_filtrada = "N/A"
    else:
        print("La lista no cumple con lo requerido para ser utilizada")

    return lista_filtrada

def ingresar_personaje(lista:list)->dict:
    '''
    Brief: La funcion pide ingresar un numero entero, siendo cada numero un personaje de DBZ
    Parameters: lista -> la lista que usaremos para mostrarla y poder elegir el nombre de un personaje
    Retorno: retorno un diccionario, el personaje seleccionado
    '''
    bandera = False

    if(type(lista) == list and len(lista) > 0):
        print("\nIndice:\n")
        for i, personaje in enumerate(lista):
            print(f"{i}, Nombre: {personaje['nombre']}")

        while bandera == False:
            respuesta = input("\nIngrese una personaje segun el indice: ")
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

def conseguir_ganador_batalla(personaje_seleccionado:dict, personaje_random:dict, clave:str)->dict:
    '''
    Brief: Funcion en donde se comparan los poderes de ataque y gana quien mayor poder tenga
    Parameters: personaje_seleccionado -> personaje seleccionado en funcion anterior
                personaje_random -> personaje random que obtuvo la maquina
    Retorno: retorno el personaje ganador de la pelea 
    '''
    if (type(personaje_seleccionado) == dict and type(personaje_random) == dict):
        if personaje_seleccionado[clave] > personaje_random[clave]:
            personaje_ganador = personaje_seleccionado
        else:
            personaje_ganador = personaje_random
    
    print("\n#----------------Batalla_finalizada----------------#\n")
    print(f"El ganador es -> {personaje_ganador['nombre']}")

    return personaje_ganador

def ingreso_dato_usuario(lista:list, cadena:str)->str:
    '''
    Biref: El usuario ingresa un dato y se recorre la lista comprobando que el dato ingresado este en la misma
    Parameters: lista -> lista que usaremos para verificar que el dato ingresado se encuentre en la misma
                cadena -> paso por parametro la pregunta que usare en el input(), asi puedo reutilizarla funcion para pedir otro ingreso de dato
                clave -> clave del diccionario
    Retorno: retorno dato ingresado
    '''
    encuentro = 0
    apruebo_respuesta = False

    if(type(lista) == list and len(lista) > 0):
        while apruebo_respuesta == False:
            imprimir_dato(lista)
            respuesta = input(f"{cadena}")
            for dato in lista:
                if respuesta == dato:
                    apruebo_respuesta = True 
                    encuentro = 1  
                    continue 
            if encuentro != 1:
                print("No se ha encontrado el dato ingresado en la lista")       

    return respuesta

def filtro_funciones(lista:list, clave:str)->list:
    '''
    Brief: Transforma una lista de datos repetidos, en una lista filtrada
    Parameters: lista -> lista que filtraremos
                clave -> valores que sera almacenados en la lista
    Retorno: retorno la lista filtrada
    '''
    lista_datos = cargar_lista_dato(lista, clave)
    lista_datos_filtrada = set(lista_datos)
    lista_datos = list(lista_datos_filtrada)

    return lista_datos

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

def formatear_habilidades(lista:list, habilidad_ingresada:str)->str:
    '''
    Brief: Formateamos la cadena y la retornamos
    Parameters: lista -> lista de habilidades
                habilidad_ingresada -> respuesta ingresada por el usuario
    Retorno: retorno la cadena formateada
    '''
    lista_nueva = []
    cadena_formateada = "N/A"

    if(type(lista) == list and len(lista) > 0):
        for cadena in lista:
            lista_nueva.append(cadena.strip())
        if habilidad_ingresada in lista_nueva:
            lista_nueva.remove(habilidad_ingresada)
            if len(lista_nueva) > 1:
                separador = ", "
                cadena = re.sub(",\s*", separador, ", ".join(lista_nueva))
                cadena_formateada = re.sub(", "," + ",cadena)        
            else:
                cadena_formateada = "".join(str(lista_nueva[0]))
        else:
            print("Esa habilidad no se encuentra en las habilidades buscadas")

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
    Brief: En una lista nueva cargamos un dato especifico de la lista de diccionarios
    Paramterers: lista -> lista que recorreremos para cargar datos en nueva lista
                clave -> dato de clave que utilizaremos para cargar en la nueva lista
    Retorno: nueva lista de datos
    '''
    lista_dato = []

    if(type(lista) == list and len(lista) > 0):
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
        for valor in dato:
            print(f"{valor}")
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