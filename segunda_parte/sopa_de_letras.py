from armado_de_tableros import Programa

class Obtener_Datos: 
    def obtener_datos_del_usuario(base_de_datos, archivo):
        palabra = input('Coloque el nombre de usuario ya registrado, si no está registrado coloque "siguiente". Recuerde que tiene que tener un largo menor a 40 caracteres: ').lower()
#!      while no se que poner.
        if palabra == "siguiente":
            print ("A continuación podrá cargar su usuario y crear su sopa de letras.")
        elif palabra in base_de_datos:
            palabra = archivo
            return archivo
        else:
            palabra = print ("No colocó el largo requerido.")

class Juego:
    def crear():
        pass
    def imprimir():
        pass
    def encontrar_palabra(nom, lista):
        max = len(lista)
        min = 0

        while max > min:
            medio = (max - min) // 2 + min
            if lista [medio] == n:
                return True
            elif n < lista [medio]: # ir a la parte izquierda
                max = medio
            else: #ir a la parte derecha
                min = medio
        return False
    def terminar_juego():
        pass
    def agregar_jugador():
        pass

class Jugador:
    def crear():
        pass
    def sumar_punto():
        pass
    def imprimir_puntaje():
        pass
    


class Palabra:
    def crear():
        pass
    
    def obtener_palabra():
        pass

class Tablero:
    def crear():
        pass

    def imprimir():
        pass

    #!Falta modificar la busqueda binaria.
    def encontrar_palabra (nom, lista):
        max = len(lista)
        min = 0

        while max > min:
            medio = (max - min) // 2 + min
            if lista [medio] == n:
                return True
            elif n < lista [medio]: # ir a la parte izquierda
                max = medio
            else: #ir a la parte derecha
                min = medio
        
        for palabra_encontrada in tablero: #! No me termina de cerrar....
            if palabra_encontrada == str(palabra_encontrada).lowerCase:
                palabra_encontrada = str(palabra_encontrada).uperCase


class Programa:
    def main():
        pass