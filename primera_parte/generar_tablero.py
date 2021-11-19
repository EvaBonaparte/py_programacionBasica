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
        index_c = random.randrange(2, N-(N/3))
        index_f = random.randrange(N)
        index_inicialC = index_c
        index_inicialF = index_f

        letras_sueltas = list(palabra)
        for letra in letras_sueltas:
            tablero[index_c][index_f] = letra
            index_c += 1
        respuestas[palabra] = {
            "x_inicial": index_inicialC, 
            "y_inicial" : index_inicialF,
            "x_final": index_c, 
            "y_final" : index_f,
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
    