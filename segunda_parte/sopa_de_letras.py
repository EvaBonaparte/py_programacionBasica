import string
import csv
from armado_de_tableros import Obtener_Datos #Para tener el metodo para pedir datos_usuario
from armado_de_tableros import Programa
from segunda_parte.funciones_sueltas import C


#TODO: Este programa permite jugar con los tableros/sopas de letras creados en el programa armado_de_tableros.py
#TODO: Funciona de la siguiente manera: Pide al usuario nombre y tablero a usar (hace validaciones). Muestra al usuario el tablero elegido y luego le pide que ingrese las palabras que encuentra. 
#TODO: Una vez encontradas esas palabras, reimprime el tablero pero esta vez con la palabra en mayuscula. El juego termina una vez que se encontraron todas las palabras o el usuario decide terminar el juego.
#TODO: Por último se devuelve el nombre del usuario + puntaje del usuario (cuantas palabras encontradas en relación a cuantas palabras había), y también dos listas: Una con las palabras encontradas en el orden que fueron encontradas y otra lista con las palabras que faltaron encontrar (si las hay) en orden alfabetico. 

class Buscar_Archivo:
    def __init__(self, sopa_de_letras, nombre_archivo):
        self.sopa_de_letras = sopa_de_letras
        self.nombre_archivo = nombre_archivo

    def validacion_archivo(self):
        try:
            f = open(self.nombre_archivo)
            print('El archivo con la sopa de letras se abrió correctamente.')
            f.close()
        except:
            print('La sopa de letras buscada no existe, por favor coloque otro nombre: ')
            self.validacion_archivo()
            return False

        return True
    
    def busqueda_archivo(self):
        self.validacion_archivo(self.nombre_archivo)

class Juego: # Esta clase es para jugar el programa. Imprime el tablero inicial y termina el juego. La busqueda de palabras y la reimpresión de tableros va en otras clases.
    #También agrega el jugador/usuario.
    def __init__(self, nombre_archivo, diccionario):
        self.nombre_archivo = nombre_archivo
        self.diccionario = diccionario
        pass

    def imprimir(self): #imprime el tablero del archivo encontrado.
        with open(self.nombre_archivo, newline='') as self.tablero:
            self.tablero = csv.reader(self.tablero)
            for fila in self.tablero:
                print(fila)
        
    def encontrar_palabra(self): #Busca la palabra
        if self.palabra_usuario in self.diccionario:
            print()
    
    def pedir_palabras(self): #Pide las palabras constantemente hasta que se coloca "fin"
        self.palabra = Palabra.palabra_usuario
        if self.palabra != 'fin':
            #! CORRER TABLERO, ETC
            pass
        else:
            print('El juego terminó, gracias por jugar. Los resultados son: ')

    def terminar_juego(self):
        #! Atención
        #? Reutilizo el código de cargar palabras? 
        pass
    def agregar_jugador(self):
        #! No me termina de cerrar.
        #? Para que llamo acá al usuario?
        print(Obtener_Datos.obtener_datos_del_usuario(self))

class Jugador:
    def __init__(self, usuario, lista_palabras_encontradas, lista_palabras_no_encontradas):
        self.usuario = usuario
        self.lista_palabras_encontradas = lista_palabras_encontradas
        self.lista_palabras_no_encontradas = lista_palabras_no_encontradas
        pass
    def resta(self, a, b):
        c = a -  b 
        return c
    def sumar_punto(self):
        self.puntos_total = len(self.lista_palabras_encontradas)
        self.puntos_a_restar = len(self.lista_palabras_no_encontradas)
        self.puntos_resultado = self.resta(self.lista_palabras_encontradas, self.lista_palabras_no_encontradas)
        return self.puntos_resultado
    def imprimir_puntaje(self):
        print('El puntaje final del juego para ', self.usuario ,' es: ', self.sumar_punto(), ' puntos.')
    


class Palabra:
    def __init__(self):
        pass
    
    def obtener_palabra(self):
        self.palabra_usuario = input('Coloque la palabra que encontró: ')
        return self.palabra_usuario
    

class Tablero:
    def __init__(self, nombre_archivo):
        self.nombre_archivo = nombre_archivo

    def imprimir(self):
        pass


    #!Falta modificar la busqueda binaria.
    def encontrar_palabra (self, nom, lista):
        max = len(lista)
        min = 0

        while max > min:
            medio = (max - min) // 2 + min
            if lista [medio] == self.n:
                return True
            elif self.n < lista [medio]: # ir a la parte izquierda
                max = medio
            else: #ir a la parte derecha
                min = medio
        
        for palabra_encontrada in self.tablero: #! No me termina de cerrar....
            if palabra_encontrada == str(palabra_encontrada).lowerCase:
                palabra_encontrada = str(palabra_encontrada).uperCase


class Programa:
    def main():
        usuario = Obtener_Datos.pedir_datos_usuario()        
        Buscar_Archivo.busqueda_archivo()

        Jugador(usuario, lista_palabras_encontradas, lista_palabras_no_encontradas)
        puntaje = Jugador.imprimir_puntaje()



Programa.main()