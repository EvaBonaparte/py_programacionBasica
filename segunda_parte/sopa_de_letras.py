from armado_de_tableros import Obtener_Datos


#TODO: Este programa permite jugar con los tableros/sopas de letras creados en el programa armado_de_tableros.py
#TODO: Funciona de la siguiente manera: Pide al usuario nombre y tablero a usar (hace validaciones). Muestra al usuario el tablero elegido y luego le pide que ingrese las palabras que encuentra. 
#TODO: Una vez encontradas esas palabras, reimprime el tablero pero esta vez con la palabra en mayuscula. El juego termina una vez que se encontraron todas las palabras o el usuario decide terminar el juego.
#TODO: Por último se devuelve el nombre del usuario + puntaje del usuario (cuantas palabras encontradas en relación a cuantas palabras había), y también dos listas: Una con las palabras encontradas en el orden que fueron encontradas y otra lista con las palabras que faltaron encontrar (si las hay) en orden alfabetico. 


class Juego: # Esta clase es para jugar el programa. Imprime el tablero inicial y termina el juego. La busqueda de palabras y la reimpresión de tableros va en otras clases.
    #También agrega el jugador/usuario.
    def __init__(self, nombre_archivo):
        self.nombre_archivo = nombre_archivo
        pass
    def imprimir(self): #imprime el tablero del archivo encontrado.
        with open(self.nombre_archivo, newline='') as self.tablero:
            self.tablero = csv.reader(self.tablero)
            for fila in self.tablero:
                print(fila)
        
    def encontrar_palabra(self, nom, lista):
        self.max = len(lista)
        self.min = 0

        while self.max > self.min:
            self.medio = (self.max - self.min) // 2 + min
            if self.lista [self.medio] == self.n:
                return True
            elif self.n < self.lista [self.medio]: # ir a la parte izquierda
                self.max = self.medio
            else: #ir a la parte derecha
                self.min = self.medio
        return False
    def terminar_juego(self):
        #! Atención
        #? Reutilizo el código de cargar palabras? 
        pass
    def agregar_jugador(self):
        #! No me termina de cerrar.
        #? Para que llamo acá al usuario?
        print(Obtener_Datos.obtener_datos_del_usuario(self))

class Jugador:
    def __init__(self):
        self.usuario = Obtener_Datos.obtener_datos_del_usuario(self)
        pass
    def sumar_punto(self):
        pass
    def imprimir_puntaje(self):
        pass
    


class Palabra:
    def __init__():
        pass
    
    def obtener_palabra():
        pass

class Tablero:
    def __init__():
        pass

    def imprimir():
        pass

    #!Falta modificar la busqueda binaria.
    def encontrar_palabra (nom, lista):
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
        Obtener_Datos.pedir_datos_usuario()


Programa.main()