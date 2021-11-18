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

def main():
    lista = [2,4,6,8,11,25,30,45,50,67,78]
    n = 2
    print(Busqueda_Binaria(n, lista))

main()
