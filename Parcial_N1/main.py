#------------------Main------------------#

from os import system
from funciones import *
from archivos import *

system("cls")

menu = [
    "1-Traer datos desde archivo",
    "2-Listar cantidad por raza",
    "3-Listar personajes por raza",
    "4-Listar personajes por habilidad",
    "5-Jugar batalla",
    "6-Guardar Json",
    "7-Leer Json",
    "9-Otorgar poder a Saiyan",
    "8-Salir del programa"
]

RUTA_CSV = "C:\\Users\\rodri\\Downloads\\DBZ.csv"
RUTA_BATALLA = "C:\\Users\\rodri\\OneDrive\\Documentos\\Archivos\\Parcial_N1\\BATALLA.csv"
RUTA_SAIYAN = "C:\\Users\\rodri\\OneDrive\\Documentos\\Archivos\\Parcial_N1\\SAIYAN.csv"
ruta =  "C:\\Users\\rodri\\OneDrive\\Documentos\\Archivos\\Parcial_N1\\"

cadena_habilidad = "Ingrese una habilidad de las mostradas en la lista: "
cadena_primera = "Ingrese una raza de un personaje: "
cadena_segunda = "Ingrese una habilidad de un personaje: "
bandera_archivo = False
bandera_actualizada = False
bandera_ruta_json = False
seguir = True

while seguir == True:
    respuesta = menu_principal(menu)

    match(respuesta):
        case 1:
            if bandera_archivo == True:
                print("\nYa se trajeron los datos de archivo correctamente\n")
            else:
                lista_diccionarios = leer_csv(RUTA_CSV)
                lista_modificada = limpiar_dato(lista_diccionarios, 'habilidades')
                if lista_diccionarios != False:
                    bandera_archivo = True
                    print("\nSe trajeron los datos desde archivo correctamente\n")
                    if bandera_actualizada == True:
                        print("\nLos datos ya han sido normalizados\n")
                    else:
                        lista_actualizada = convertir_a_entero(lista_modificada)
                        bandera_actualizada = True
                        print("\nDatos normalizados\n")
                else:
                    print("¡No se pudo traer datos desde archivo correctamente!")
        case 2:
            if bandera_archivo == True and bandera_actualizada == True:
                pasaje_a_lista(lista_actualizada, 'raza')
            else:
                print("\n¡ERROR!\n¡Primero debe traer los datos desde archivo!")
        case 3:
            if bandera_archivo == True:
                if bandera_actualizada == True:
                    listar_agrupados(lista_actualizada, 'raza')
                else:
                    print("\n¡ERROR!\n¡Debes normalizar los datos primero!")
            else:
                print("\n¡ERROR!\n¡Primero debe traer los datos desde archivo!")
        case 4:
            if bandera_archivo == True and bandera_actualizada == True:
                habilidad_ingresada = ingresar_habilidad(lista_actualizada, cadena_habilidad, 'habilidades')
                buscar_personajes_habilidad(lista_actualizada, habilidad_ingresada, 'habilidades')
            else:
                print("\n¡ERROR!\n¡Primero debe traer los datos desde archivo!")
        case 5:
            if bandera_archivo == True and bandera_actualizada == True:
                personaje_seleccionado = ingresar_personaje(lista_actualizada)
                personaje_random = seleccionar_personaje_random(lista_actualizada)
                personaje_ganador = conseguir_ganador_batalla(personaje_seleccionado, personaje_random, 'poder_ataque')
                if personaje_ganador != personaje_seleccionado:
                    personaje_perdedor = personaje_seleccionado
                else:
                    personaje_perdedor = personaje_random
                fecha_actual = conseguir_fecha_actual()
                generar_csv(RUTA_BATALLA, fecha_actual, personaje_ganador, personaje_perdedor)
            else:
                print("\n¡ERROR!\n¡Primero debe traer los datos desde archivo!")
        case 6:
            if bandera_archivo == True and bandera_actualizada == True:
                habilidad_ingresada = ingresar_habilidad(lista_actualizada, cadena_habilidad, 'habilidades')
                lista_clave = filtro_funciones(lista_actualizada, 'raza')
                raza_ingresada = ingreso_dato_usuario(lista_clave, cadena_primera)
                cadena_json = formato_cadenas(raza_ingresada, habilidad_ingresada)
                listado_flitrada = buscar_personajes_cumplen(lista_actualizada, raza_ingresada, habilidad_ingresada)
                if listado_flitrada != "N/A":
                    lista_formateada = formatear_lista(listado_flitrada, habilidad_ingresada)
                    ruta_json = formato_ruta(ruta ,cadena_json)
                    retorno = generar_json(ruta_json, lista_formateada)
                    if retorno != -1:
                        bandera_ruta_json = True
                        print("\nSe cargaron correctamente los datos")
                    else:
                        print("Algo salio mal al generar el json")
            else:
                print("\n¡ERROR!\n¡Primero debe traer los datos desde archivo!")
        case 7:
            if bandera_ruta_json == True:
                leer_json(ruta_json)
            else:
                print("\n¡ERROR!\n¡Primero debe guardar el archivo json!")
        case 8:
            seguir = False
            print(f"\nUsted ha salido del menu")
        case 9:
            if bandera_archivo == True and bandera_actualizada == True:
                lista_saiyan = otorgar_poder_saiyan(lista_actualizada, 'Saiyan')
                generar_nuevo_csv(RUTA_SAIYAN, lista_saiyan)
                print("\nSe cargaron en un archivo correctamente los datos\n")
            else:
                print("\n¡ERROR!\n¡Primero debe traer los datos desde archivo!")
        case _:
            print(f"\n¡ERROR!\n¡Esta opcion no existe!\nReingrese su opcion de menu")