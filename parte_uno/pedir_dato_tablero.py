import string
import csv

# validaciones
def validacion (dato_pedido, condicion):
    while dato_pedido != 0: 
        if dato_pedido >= condicion:
            return print(dato_pedido)
        else:
            dato_pedido = int(input("Vuelva a colocar el dato nuevamente: "))
    return


#pedir dato tablero
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


