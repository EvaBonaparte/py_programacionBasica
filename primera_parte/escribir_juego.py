from os import write
import string
import csv
from pedir_dato_tablero import pedir_datos_tablero
from generar_tablero import generar_tablero


def crear_archivo(texto, tablero):
    texto = open( texto + '.csv', 'w')
    writer = csv.writer(texto + '.csv', delimiter = ',')
    writer.writerows(tablero)
    texto.close()
    return texto

def crear_solucion(texto, diccionario, tablero):
    texto = texto + "_solucion"
    texto = open( texto + '.csv', 'w')
    texto = (texto + '.csv', 'w')
    writer = csv.writer(tablero, delimiter = ',')
    writer.writerows(tablero)
    writer.writerows(diccionario)
    texto.close()
    return texto

def escribir_juego(nombre_archivo, tablero, diccionario):
    # Crear nombre del archivo
    texto = nombre_archivo   
    sopa_letras = crear_archivo(texto, tablero)
    sopa_letras_solucion = crear_solucion(texto, diccionario, tablero)
    return sopa_letras, sopa_letras_solucion
    
    



def main():
    N, var_palabras, nombre_archivo = pedir_datos_tablero()
    tablero, respuestas = generar_tablero(N, var_palabras)
    escribir_juego(nombre_archivo, tablero, respuestas)
    return

main()