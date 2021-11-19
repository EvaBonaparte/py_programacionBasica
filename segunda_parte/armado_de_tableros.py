from os import write
import string
import random
import csv

class Programa:
    def main():
        pass

class Escritor:
    def crear_archivo(texto, tablero): 
        with open(texto +'.csv', 'w', newline='') as archivo1:
            archivo1 = csv.writer(archivo1)
            archivo1.writerows(tablero)
        return archivo1

    def crear_solucion(texto, diccionario, tablero):
        with open(texto + '_solucion.csv', 'w', newline='') as nombre_archivo:
            archivo2 = (texto + '_solucion.csv', 'a')
            archivo2 = csv.writer(archivo2)
            archivo2 = csv.DictWriter(diccionario, delimiter = ',')
            archivo2 = (tablero)
        return archivo2

class Generador_Tableros:
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

class Obtener_Datos:
    def validacion (dato_pedido, condicion):
        while dato_pedido != 0: 
            if dato_pedido >= condicion:
                return print(dato_pedido)
            else:
                dato_pedido = int(input("Vuelva a colocar el dato nuevamente: "))
        return

    def pedir_datos_tablero ():
        # Numero entero
        N = int(input("Seleccione una cantidad de filas y columnas mayor o igual a 15: "))
        validacion(N, 15)

        #var_palabra es la variable que voy a usar para medir la longitud y la cantidad minima de palabras
        var_palabra = int(N / 3)
        #pedir las palabras, fijar la cantidad máxima de palabras y su longitud. Se valida solo 
        lista_palabras = []
        print("Acontinuación coloque una palabra que tenga menos de ", var_palabra, " letras.")
        print ("Si quiere terminar la carga de palabras coloque la palabra 'fin'")
        palabra= ""
        while len(lista_palabras) < (var_palabra - 1) and palabra != "fin":
            palabra = input("Coloque una palabra: ").lower()
            if palabra == "fin":
                print ("Ya termino la carga de palabras.")
            elif len(palabra) < var_palabra:
                lista_palabras.append(palabra)
            else:
                palabra = print ("No colocó el largo requerido.")

        print(lista_palabras)

        # Toma nombre archivo y validación
        nombre_archivo = str(input("Coloque a continuación el nombre del archivo que va a almacenar sus datos (no debe ser mayor a 30 caracteres): "))
        while len(nombre_archivo) > 30:
            print("Cantidad de caracteres no valida")
            nombre_archivo = str(input("Coloque nuevamente un nombre de archivo con menos de 30 letras: "))
            if len(nombre_archivo) < 30:
                break
                        
        #creación tupla
        tupla=(N, lista_palabras, nombre_archivo)    
        return (tupla)

    def pedir_datos_usuario():
        #!Falta completar
        pass


