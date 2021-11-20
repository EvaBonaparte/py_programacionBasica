from armado_de_tableros import Programa

class Obtener_Datos: 
    def obtener_datos_del_usuario(self, base_de_datos, archivo):
        self.palabra = input('Coloque el nombre de usuario ya registrado, si no está registrado coloque "siguiente". Recuerde que tiene que tener un largo menor a 40 caracteres: ').lower()
#!      while no se que poner.
        if self.palabra == "siguiente":
            print ("A continuación podrá cargar su usuario y crear su sopa de letras.")
        elif self.palabra in self.base_de_datos:
            self.palabra = archivo
            return archivo
        else:
            self.palabra = print ("No colocó el largo requerido.")

class Juego:
    def crear(self):
        pass
    def imprimir(self):
        pass
    def encontrar_palabra(self, nom, lista):
        self.max = len(lista)
        self.min = 0

        while self.max > self.min:
            self.medio = (self.max - self.min) // 2 + min
            if self.lista [self.medio] == n:
                return True
            elif self.n < self.lista [self.medio]: # ir a la parte izquierda
                self.max = self.medio
            else: #ir a la parte derecha
                self.min = self.medio
        return False
    def terminar_juego(self):
        pass
    def agregar_jugador(self):
        pass

class Jugador:
    def crear(self):
        pass
    def sumar_punto(self):
        pass
    def imprimir_puntaje(self):
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