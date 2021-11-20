def Busqueda_Binaria (n, lista):
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

# Hacer manejo de excepciones (aviso de errores)

def C(): #Función que me interesa llamar, ej: Abrir
    raise Exception ('Esto es un error.')

def B(): #Función que prueba llamar a 
    return C()

def A(): #probar hacer lo que está en el bloque
    try:
        return B()
    except: #Si falla hacer lo siguiente
        print ('Ocurrio un error.')




def main():
    # Lo que necesito para que la busqueda binaria sirva: 
    lista = [2,4,6,8,11,25,30,45,50,67,78]
    n = 2
    print(Busqueda_Binaria(n, lista))

    #Lo que necesito para que hacer manejo de excepciones (aviso de errores) sirva: 
    A()

main()
