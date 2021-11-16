from os import write
import string
import csv
from pedir_dato_tablero import pedir_datos_tablero
from generar_tablero import generar_tablero




def escribir_juego(nombre_archivo, tablero, diccionario):
    # Crear nombre del archivo
    texto = nombre_archivo
    texto = open('texto.csv', 'w')
    writer = csv.writer(texto.csv, delimiter = ',')
    writer.writerows(tablero)
    texto.close()
    texto2 = nombre_archivo + "_solucion"
    texto2 = ('texto2.csv', 'w')
    writer = csv.writer(tablero, delimiter = ',')
    writer.writerows(tablero)
    writer.writerows(diccionario)
    texto2.close()



def main():
    N, var_palabras, nombre_archivo = pedir_datos_tablero()
    tablero, respuestas = generar_tablero(N, var_palabras)
    escribir_juego(nombre_archivo, tablero, respuestas)



    return

main()