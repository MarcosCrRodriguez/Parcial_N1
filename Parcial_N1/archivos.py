#------------------Archivos------------------#

import csv
import json

def leer_csv(RUTA_CSV:str)->list:
    '''
    Brief: Lee un archivo csv, en el que tomo la informacion y lo transformo en una lista de diccionarios
    Parameters: RUTA_CSV -> donde esta hubicado el archivo csv
    Retorno: lista_retorno -> retorno la lista de listas
    '''
    lista_diccionarios = []

    with open(RUTA_CSV, 'r', encoding='utf-8') as archivo: 
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

def generar_saiyan_csv(RUTA_SAIYAN:str, lista_saiyan:list)->None:
    '''
    Brief: Genero un archivo csv, en donde cargo los datos pasados por parametros
    Parameters: RUTA_SAIYAN -> donde se guardara el archivo csv
                lista_saiyan -> lista de diccionarios que mostrare en el archivo
    '''
    with open(RUTA_SAIYAN, 'w', newline='', encoding='utf-8') as archivo:
        escritor = csv.writer(archivo) 
        for personaje in lista_saiyan:
            fila = [personaje['id'],
                    personaje['nombre'],
                    personaje['raza'],
                    personaje['poder_ataque'],
                    personaje['poder_pelea'],
                    personaje['habilidades']]
            escritor.writerow(fila) 

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