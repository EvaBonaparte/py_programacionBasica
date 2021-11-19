from os import write
import string
import csv
from pedir_dato_tablero import pedir_datos_tablero
from generar_tablero import generar_tablero


def escribir_juego(nombre_archivo, tablero, diccionario):
    # Crear nombre del archivo
    texto = nombre_archivo   
    with open(texto +'.csv', 'w', newline='') as archivo1:
        archivo1 = csv.DictWriter(write(str(tablero)), delimiter = ',')
        archivo1.writerows(tablero)
    with open(texto + '_solucion.csv', 'w', newline='') as nombre_archivo:
        archivo2 = (texto + '_solucion.csv', 'a')
        archivo2 = csv.DictWriter(write(str(tablero, diccionario)), delimiter = ',')
        archivo2 = (tablero)

    return archivo1, archivo2
    
    



def main():
    N, var_palabras, nombre_archivo = pedir_datos_tablero()
    print('hola')
    tablero, respuestas = generar_tablero(N, var_palabras)
    print('chau')
    escribir_juego(nombre_archivo, tablero, respuestas)
    print('papas')
    return

main()