def validar(dato):
    return int(dato)>=15


def pedir_dato(texto, val):
    dato = int(input(texto))
    while not val(dato):
        dato = int(input(texto))
    return dato


def main():
    funcion = validar
    print(pedir_dato("Ingresar un numero mayor o igual a 15: ", funcion))
    return 

main()
