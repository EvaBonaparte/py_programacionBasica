from os import write
import string
import random
import csv

from trabajoFinal.segunda_parte.sopa_de_letras import Tablero

class Programa:
    def main():
        pass

class Escritor:
    def __init__(self, diccionario, texto):
        self.texto = texto
        self.diccionario = diccionario
        return
    def crear_archivo(self): 
        with open(self.texto +'.csv', 'w', newline='') as archivo1:
            archivo1 = csv.writer(archivo1)
            archivo1.writerows(self.tablero)
        return archivo1

    def crear_solucion(self):
        with open(self.texto + '_solucion.csv', 'w', newline='') as nombre_archivo:
            archivo2 = (self.texto + '_solucion.csv', 'a')
            archivo2 = csv.writer(archivo2)
            archivo2 = csv.DictWriter(self.diccionario, delimiter = ',')
            archivo2 = (self.tablero)
        return archivo2

class Generador_Tableros:
    def __init__(self, N, var_palabras):
        self.N = N
        self.var_palabras = var_palabras


    def generar_tablero(self):
        self.tablero = []
        self.respuestas = {}
        for j in range(0,self.N): #cantidad de filas
            self.tablero.append([])
        # iteramos x cada cuadrado de la matriz
        for j in range(0,self.N): #cantidad de columnas
            for i in range(0,self.N):
                self.tablero[i].append(-1)        
        # Acá van puestas las palabras de forma vertical.
        for self.palabra in self.var_palabras:
            self.index_c = random.randrange(2, self.N-(self.N/3))
            self.index_f = random.randrange(self.N)
            self.index_inicialC = self.index_c
            self.index_inicialF = self.index_f

            self.letras_sueltas = list(self.palabra)
            for self.letra in self.letras_sueltas:
                self.tablero[self.index_c][self.index_f] = self.letra
                self.index_c += 1
            self.respuestas[self.palabra] = {
                "x_inicial": self.index_inicialC, 
                "y_inicial" : self.index_inicialF,
                "x_final": self.index_c, 
                "y_final" : self.index_f,
            }
        # #Recorrer la matriz:
        self.l = 0
        self.j = 0
        for self.l in range(0,self.N):
            for self.j in range(0,self.N):
                if self.tablero [self.l][self.j] == -1 :
                    self.tablero [self.l][self.j] = random.choice(string.ascii_lowercase)

        separador = " | "
        for x in self.tablero: 
            print(separador.join(map(str,x))) 
        
        return self.tablero, self.respuestas

class Obtener_Datos:
    def __init__(self, dato_pedido, condicion):
        self.dato_pedido = dato_pedido
        self.condicion = condicion

    def validacion (self):
        while self.dato_pedido != 0: 
            if self.dato_pedido >= self.condicion:
                return print(self.dato_pedido)
            else:
                self.dato_pedido = int(input("Vuelva a colocar el dato nuevamente: "))
        return

    def pedir_datos_tablero (self):
        # Numero entero
        N = int(input("Seleccione una cantidad de filas y columnas mayor o igual a 15: "))
        self.validacion(N, 15)

        #var_palabra es la variable que voy a usar para medir la longitud y la cantidad minima de palabras
        self.var_palabra = int(N / 3)
        #pedir las palabras, fijar la cantidad máxima de palabras y su longitud. Se valida solo 
        self.lista_palabras = []
        print("Acontinuación coloque una palabra que tenga menos de ", self.var_palabra, " letras.")
        print ("Si quiere terminar la carga de palabras coloque la palabra 'fin'")
        self.palabra= ""
        while len(self.lista_palabras) < (self.var_palabra - 1) and self.palabra != "fin":
            self.palabra = input("Coloque una palabra: ").lower()
            if self.palabra == "fin":
                print ("Ya termino la carga de palabras.")
            elif len(self.palabra) < self.var_palabra:
                self.lista_palabras.append(self.palabra)
            else:
                self.palabra = print ("No colocó el largo requerido.")

        print(self.lista_palabras)

        # Toma nombre archivo y validación
        self.nombre_archivo = str(input("Coloque a continuación el nombre del archivo que va a almacenar sus datos (no debe ser mayor a 30 caracteres): "))
        while len(self.nombre_archivo) > 30:
            print("Cantidad de caracteres no valida")
            self.nombre_archivo = str(input("Coloque nuevamente un nombre de archivo con menos de 30 letras: "))
            if len(self.nombre_archivo) < 30:
                break
                        
        #creación tupla
        self.tupla=(N, self.lista_palabras, self.nombre_archivo)    
        return self.tupla

    def pedir_datos_usuario(self):
        self.usuario = str(input("Coloque a continuación el nombre de usuario con el que se vá a loguear (no debe ser mayor a 40 caracteres): "))
        while len(self.usuario) > 40:
            print("Cantidad de caracteres no valida")
            self.usuario = str(input("Coloque nuevamente un nombre de usuario con menos de 40 letras: "))
            if len(self.usuario) < 40:
                break


