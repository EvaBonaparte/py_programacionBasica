import string
import csv



#TODO: Este programa permite jugar con los tableros/sopas de letras creados en el programa armado_de_tableros.py
#TODO: Funciona de la siguiente manera: Pide al usuario nombre y tablero a usar (hace validaciones). Muestra al usuario el tablero elegido y luego le pide que ingrese las palabras que encuentra. 
#TODO: Una vez encontradas esas palabras, reimprime el tablero pero esta vez con la palabra en mayuscula. El juego termina una vez que se encontraron todas las palabras o el usuario decide terminar el juego.
#TODO: Por último se devuelve el nombre del usuario + puntaje del usuario (cuantas palabras encontradas en relación a cuantas palabras había), y también dos listas: Una con las palabras encontradas en el orden que fueron encontradas y otra lista con las palabras que faltaron encontrar (si las hay) en orden alfabetico. 

class Obtener_Datos:
    def __init__(self):
        pass

    def pedir_datos_usuario(self): #Acá pido el nombre de usuario para crear una base de datos de usuarios y luego poder ingresarlo cada vez que juego
        usuario = str(input("Coloque a continuación el nombre de usuario con el que se vá a loguear (no debe ser mayor a 40 caracteres): "))
        while len(usuario) > 40:
            print("Cantidad de caracteres no valida")
            usuario = str(input("Coloque nuevamente un nombre de usuario con menos de 40 letras: "))
            if len(usuario) < 40:
                break
        nombre_archivo = str(input("Coloque a continuación el nombre del archivo que contiene la sopa de letras que va a jugar (no debe ser mayor a 30 caracteres): "))
        while len(nombre_archivo) > 30:
            print("Cantidad de caracteres no valida")
            nombre_archivo = str(input("Coloque nuevamente un nombre de archivo con menos de 30 letras: "))
            if len(nombre_archivo) < 30:
                break
        return usuario, nombre_archivo

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
    def __init__(self, usuario, nombre_archivo, lista_palabras_encontradas, lista_palabras_no_encontradas, lista_palabras_tablero, tablero, puntaje, palabra):
        self.usuario = usuario
        self.nombre_archivo = nombre_archivo
        self.lista_palabras_encontradas = lista_palabras_encontradas
        self.lista_palabras_no_encontradas = lista_palabras_no_encontradas
        self.lista_palabras_tablero = lista_palabras_tablero
        self.tablero = tablero
        self.puntaje = puntaje
        self.palabra = palabra

    def __str__(self):
        print('Instrucciones: El juego consiste en que puedas jugar alguna de las sopas de letras ya creadas. Para eso vas a tener que colocar un nombre de usuario y el nombre de la sopa de letra que querés jugar. Una vez hecho este paso vas a ver el tablero, cuando encuentres una palabra... ¡Escribila! Después de escribir la palabra (si esta se encontraba en el tablero) se va a volver a mostrar el tablero con la palabra que encontraste en MAYUSCULA. Así hasta que pongas "fin" o encuentres todas las palabras. Una vez terminado se te va a devolver el puntaje que es la cantidad de palabras encontradas en la sopa de letras ¡Buena suerte y a jugar!')

    def imprimir(self): #imprime el tablero del archivo encontrado.
        self.nombre_archivo = self.nombre_archivo , '_solucion'
        with open(self.nombre_archivo, newline='') as self.archivo:
            self.tablero = csv.reader(self.tablero)
            self.diccionario = csv.reader(self.diccionario)
            for fila in self.tablero:
                print(fila)
            return self.tablero, self.diccionario
        
    def encontrar_palabra(self): #Busca la palabra
        if self.palabra in self.diccionario:
            print()
    
    def pedir_palabras(self): #Pide las palabras constantemente hasta que se coloca "fin"
        for self.palabra in self.tablero:
            if self.palabra != 'fin':
                Tablero().verifica_palabra()
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
            print ('Las palabras que sí encontraste fueron: ', self.lista_palabras_encontradas)
        else:
            print('¡Felicitaciones! Encontraste todas las palabras de la sopa de letras.')


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
    def __init__(self, lista_palabras_encontradas, lista_palabras_tablero):
        self.lista_palabras_encontradas = lista_palabras_encontradas
        self.lista_palabras_tablero = lista_palabras_tablero
        pass
    
    def obtener_palabra(self):
        while len(self.lista_palabras_encontradas) != len(self.lista_palabras_tablero) or Palabra().obtener_palabra() != "fin":
            self.palabra_usuario = input('Coloque la palabra que encontró: ')
        return self.palabra_usuario
    

class Tablero:
    def __init__(self, diccionario, palabra_encontrada, tablero, diccionario_claves):
        self.diccionario = diccionario
        self.palabra_encontrada = palabra_encontrada
        self.tablero = tablero
        self.diccionario_claves = diccionario_claves

    def imprimir(self):
        print(Tablero.pasar_mayuscula())

    def verifica_palabra(self):
        for key in self.diccionario:
            if self.palabra_encontrada == key:
                self.lista_palabras_encontradas = self.lista_palabras_encontradas.append(self.palabra_encontrada)
                return self.lista_palabras_encontradas
        return print('Esa palabra no está en la sopa de letras o está mal escrita.')

    def pasar_mayuscula(self): # Tendría que poder usar las coordenadas del diccionario para constatar el lugar de la palabra y por ende cada letra pero no se me ocurre como.
        for self.palabra_encontrada in self.diccionario.keys():
            valores = self.palabra_encontrada.key()
            x_inicial, y_inicial, x_final, y_final = valores
            if x_inicial == x_final:
                while y_inicial != y_final:
                    y = y_inicial
                    x = x_inicial
                    self.tablero[y][x].upper()
                    y += 1
            else: 
                while x_inicial != x_final:
                    y = y_inicial
                    x = x_inicial
                    self.tablero[y][x].upper()
                    x += 1    
        return self.tablero
    


class Programa:
    def main():
        Juego.__str__()
        usuario, nombre_archivo = Obtener_Datos().pedir_datos_usuario()    
        lista_palabras_encontradas = []
        lista_palabras_no_encontradas = []
        puntaje = Jugador().imprimir_puntaje()
        tablero, diccionario = Juego().imprimir()
        palabra_encontrada = Palabra().obtener_palabra()
        lista_palabras_tablero = [] #Falta completar
        Juego(usuario, nombre_archivo, lista_palabras_encontradas, lista_palabras_no_encontradas, lista_palabras_tablero, tablero, puntaje, palabra_encontrada)
        Tablero(diccionario, palabra_encontrada, tablero)
        Jugador(usuario, lista_palabras_encontradas, lista_palabras_no_encontradas)




Programa.main()