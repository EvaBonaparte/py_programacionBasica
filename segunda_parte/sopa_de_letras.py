import string
import csv
from armado_de_tableros import Obtener_Datos #Para tener el metodo para pedir datos_usuario
from armado_de_tableros import Generador_Tableros

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
    def __init__(self, usuario, nombre_archivo, lista_palabras_encontradas, lista_palabras_no_encontradas, puntaje):
        self.usuario = usuario
        self.nombre_archivo = nombre_archivo
        self.lista_palabras_encontradas = lista_palabras_encontradas
        self.lista_palabras_no_encontradas = lista_palabras_no_encontradas
        self.puntaje = puntaje


    def imprimir(self): #imprime el tablero del archivo encontrado.
        self.nombre_archivo = self.nombre_archivo , '_solucion'
        with open(self.nombre_archivo, newline='') as self.archivo:
            self.tablero = csv.reader(self.tablero)
            self.diccionario = csv.reader(self.diccionario)
            for fila in self.tablero:
                print(fila)
            return self.tablero, self.diccionario
        
    def encontrar_palabra(self): #Busca la palabra
        if self.palabra_usuario in self.diccionario:
            print()
    
    def pedir_palabras(self): #Pide las palabras constantemente hasta que se coloca "fin"
        self.palabra = Palabra.palabra_usuario
        if self.palabra != 'fin':
            #! CORRER TABLERO, ETC
            pass
        else:
            print('La carga de palabras terminó con éxito.')

    def terminar_juego(self):
        for self.palabra in self.lista_palabras_tablero:
            if self.palabra not in self.lista_palabras_encontradas:
                self.lista_palabras_no_encontradas.append(self.palabra)
            else:
                break
        if len(self.lista_palabras_no_encontradas) != 0:
            self.lista_palabras_no_encontradas.sort()
            print ('¡Upa! Te faltaron encontrar las siguientes palabras: ', self.lista_palabras_no_encontradas , '. Recordá que cada palabra vale un punto y que las palabras no encontradas se le restan total de las palabras.')
        else:
            print('¡Felicitaciones! Encontraste todas las palabras de la sopa de letras.')

    def agregar_jugador(self):
        #! No me termina de cerrar.
        #? Para que llamo acá al usuario?
        self.saludo = '¡Hola ' , self.usuario , '! ¡Bienvenidx!'
        print(self.saludo)

class Jugador:
    def __init__(self, usuario, lista_palabras_encontradas, lista_palabras_tablero):
        self.usuario = usuario
        self.lista_palabras_encontradas = lista_palabras_encontradas
        self.lista_palabras_tablero =  lista_palabras_tablero

    def sumar_punto(self):
        self.puntos_total = len(self.lista_palabras_tablero)
        self.puntos_palabras_encontradas = self.lista_palabras_encontradas
        return self.puntos_palabras_encontradas 
    def imprimir_puntaje(self):
        print('El puntaje final del juego para ', self.usuario ,' es: ', self.sumar_punto(), ' puntos sobre ', len(self.lista_palabras_tablero))
    

class Palabra:
    def __init__(self):
        pass #? Tengo que hacer algo acá?
    
    def obtener_palabra(self):
        self.palabra_usuario = input('Coloque la palabra que encontró: ')
        return self.palabra_usuario
    

class Tablero:
    def __init__(self, diccionario, palabra_encontrada, tablero):
        self.diccionario = diccionario
        self.palabra_encontrada = palabra_encontrada
        self.tablero = tablero

    def imprimir(self):
        print(Tablero.pasar_mayuscula())

    def verifica_palabra(self):
        for key in self.diccionario:
            if self.palabra_encontrada == key:
                self.lista_palabras_encontradas = self.lista_palabras_encontradas.append(self.palabra_encontrada)
                return self.lista_palabras_encontradas
        return print('Esa palabra no está en la sopa de letras o está mal escrita.')

    def pasar_mayuscula(self): # Tendría que poder usar las coordenadas del diccionario para constatar el lugar de la palabra y por ende cada letra pero no se me ocurre como.
        self.palabra_encontrada = Tablero.verifica_palabra(self.diccionario, self.palabra_encontrada)
        for palabra_encontrada in self.tablero: #! No me termina de cerrar....
                if palabra_encontrada == str.lower(palabra_encontrada):
                    palabra_encontrada = str.upper(palabra_encontrada)
        
        return print(self.tablero)
    


class Programa:
    def main():
        usuario = Obtener_Datos.pedir_datos_usuario()        
        nombre_archivo = Buscar_Archivo.busqueda_archivo()
        lista_palabras_encontradas = []
        lista_palabras_no_encontradas = []
        puntaje = Jugador.imprimir_puntaje()
        tablero, diccionario = Juego.imprimir()
        palabra_encontrada = Palabra.obtener_palabra()
        Juego(usuario, nombre_archivo, lista_palabras_encontradas, lista_palabras_no_encontradas, puntaje)
        Tablero(diccionario, palabra_encontrada, tablero)
        Jugador(usuario, lista_palabras_encontradas, lista_palabras_no_encontradas)




Programa.main()