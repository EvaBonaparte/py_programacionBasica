import random
import string

from pedir_dato_tablero import pedir_datos_tablero
                  

def generar_tablero(N, var_palabras):
    tablero = []
    respuestas = {}
    for j in range(0,N): #cantidad de filas
        tablero.append([])
    # iteramos x cada cuadrado de la matriz
    for j in range(0,N): #cantidad de columnas
        for i in range(0,N):
            tablero[i].append(-1)        
    # Acá van puestas las palabras de forma vertical.
    for palabra in var_palabras:
        index_f = random.randrange(2, N-(N/3))
        index_c = random.randrange(N)

        letras_sueltas = list(palabra)
        respuestas[palabra] = {
            "x_inicial": index_f, 
            "y_inicial" : index_c,
        }       
        for letra in letras_sueltas:
                tablero[index_f][index_c] = letra
                index_f += 1
        respuestas[palabra] = {
            "x_final": index_f, 
            "y_final" : index_c,
        }
    # #Recorrer la matriz:
    i = 0
    j = 0
    for i in range(0,N):
        for j in range(0,N):
            if tablero [i][j] == -1 :
                tablero [i][j] = random.choice(string.ascii_lowercase)

    separador = " | "
    for x in tablero: 
        print(separador.join(map(str,x))) 
    
    return tablero, respuestas

def main():
    N, var_palabras, nombre_archivo = pedir_datos_tablero()
    generar_tablero(N, var_palabras)
    return
