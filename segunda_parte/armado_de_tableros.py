import string
import random
import csv

#TODO: Este programa trabaja con varias funciones para crear una experiencia completa de creación de sopa de letras. La sopa de letras propiamente dicha se llamará "tablero" a lo largo del código.
#TODO: El usuario deberá ingresar un número N (que será la cantidad de filas y columnas del tablero que como mínimo debe ser 15), una lista de palabras llamada var_palabras (las cuales tienen que tener un length máximo de N/3)
#TODO: También va a crear el nombre de usuario y el nombre del archivo que tendrá. Se crearán dos archivos (uno con el tablero, otro con el tablero + un diccionario con las coordenadas de cada palabra a modo de solución)


class Obtener_Datos: 
    
    #* Esta clase tiene que tener todas las funciones que tienen que ver con la toma de input, es decir, todas las funciones de validacion,
    #* pedir_dato y las dos funciones que obtienen los datos: Obtener_datos_tablero y obtener_datos_usuario.
    #* Obtener_Datos es una clase que no toma ningun argumento en el constructor.

    
    def __init__(self):
        return

    def validacion (self, dato_pedido, condicion): # Metodo que me permite validar algunos datos
        self.dato_pedido = dato_pedido
        self.condicion = condicion
        while self.dato_pedido != 0: 
            if self.dato_pedido >= self.condicion:
                return print(self.dato_pedido)
            else:
                self.dato_pedido = int(input("Vuelva a colocar el dato nuevamente: "))
        return

    def toma_numero (self):
        self.N = int(input("Seleccione una cantidad de filas y columnas mayor o igual a 15: "))
        return self.N

    def pedir_datos_tablero (self): #este metodo se encarga de pedir y validar todos los datos que necesito para crear el tablero.
        # Numero entero
        N = self.toma_numero() #! Está bien ponerle self. si es una funcion???
        self.validacion(N, 15) 

        #var_palabra es la variable que voy a usar para medir la longitud y la cantidad minima de palabras
        var_palabra = int(self.N / 3)
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
                        
        #creación tupla que contiene todos los datos creados en este método
        tupla=(N, lista_palabras, nombre_archivo)    
        return tupla



class Generador_Tableros: 
    
    #* La clase toma N y lista_palabras en el constructor, que son datos que obtuvimos desde obtener_datos_tablero (de la clase anterior).
    #* Tiene una funcion, generar, que va a retornar el tablero y el diccionario (respuestas).
    def __init__(self, N, var_palabras):
        self.N = N
        self.var_palabras = var_palabras


    def generar_tablero(self): # Crea el tablero propiamente dicho
        tipo_posicion = ["horizontal", "vertical"]
        tablero = []
        for j in range(0,self.N): #cantidad de filas
            tablero.append([])
        # iteramos x cada cuadrado de la matriz
        for j in range(0,self.N): #cantidad de columnas
            for i in range(0,self.N):
                tablero[i].append("")
        
        for palabra in self.var_palabras: #Este for itera la lista de palabras
            palabra_caracter = list(palabra)
            respuestas = {}
            index_c = random.randrange(2, self.N-(self.N/3))
            index_f = random.randrange(self.N)
            index_inicialC = index_c
            index_inicialF = index_f
            posicion = tipo_posicion[random.randint(0,1)] #Le doy la posicion a la palabra
            for l in range(0, len(palabra_caracter)): #Recorre el largo de la palabra
                if(tablero[index_c][index_f]==""): 
                    tablero[index_c][index_f] = palabra_caracter[l]
                    if(posicion == "horizontal"):    #Verifica la posicion 
                        index_f+=1
                    else:
                        index_c+=1
            respuestas[palabra] = {
                "x_inicial": index_inicialC,
                "y_inicial" : index_inicialF,
                "x_final": index_c,
                "y_final" : index_f,
                }
            
        # #Recorrer la matriz:
        i = 0
        j = 0
        for i in range(0,self.N):
            for j in range(0,self.N):
                if tablero [i][j] == "" :
                    tablero [i][j] = random.choice(string.ascii_lowercase)

        #Acá cambio los separadores de , por |
        separador = " | "
        for x in tablero: 
            print(separador.join(map(str,x))) 
        
        return tablero, respuestas


class Escritor: 
    
    #* Crea los archivos donde se va a almacenar la información. Los nombres son puestos por el usuario en la clase Obtener_Datos y están en formato csv
    #* la función crear_archivo crea un archivo solo con la sopa de letras (tablero) y crear_solucion crea un archivo con el nombre puesto por el usuario + _solucion
    #* que tiene adentro la sopa de letras (tablero) y las coordenadas de las palabras a modo de respuesta (diccionario/respuestas)
    def __init__(self, diccionario, texto, tablero):
        self.texto = texto
        self.diccionario = diccionario
        self.tablero = tablero
        return
    def crear_archivo(self): #Crea el archivo con el tablero de sopa de letras
        with open(self.texto +'.csv', 'w', newline='') as archivo1:
            archivo1 = csv.writer(archivo1)
            archivo1.writerows(self.tablero)
        return 

    def crear_solucion(self): # Crea el archivo que contiene el tablero de la sopa de letras + el diccionario con las soluciones
        with open(self.texto + '_solucion.csv', 'w', newline='') as archivo2:
            encabezado = ["palabra", "x_inicial_","y_inicial","y_final","x_final"]
            archivo2 = csv.DictWriter(self.texto, fieldnames = encabezado)
            archivo2.writeheader()
            for key,valores in self.diccionario.items():
                archivo2.writerow([key, valores])
            
        return 
    

class Programa: # Es la clase principal, permite ejecutar el armado de tableros llamando al resto de las clases del archivo.
    def main():
        N, var_palabras, nombre_archivo = Obtener_Datos().pedir_datos_tablero()
        tablero, diccionario = Generador_Tableros(N, var_palabras).generar_tablero()
        crear_los_archivos = Escritor(diccionario, nombre_archivo, tablero)
        crear_los_archivos.crear_archivo()
        crear_los_archivos.crear_solucion()

Programa.main()
