def potencia(base=10, exponente=2):
    print (base ** exponente)

resultado=potencia()
print(resultado)


def maximo(a=15, b=12, c=1):
    print (max(a, b, c))

resultado=maximo()
print(resultado)


def mostrar_rango(inicio=4, fin=9):
    for numero in range(inicio, fin+1):
        print(numero)

resultado=mostrar_rango()
print(resultado)


def decimal_a_binario(decimal=10):
    print (bin(decimal)[2:])

resultado=decimal_a_binario()
print(resultado)


def area_circulo(radio=4):
    print (3.14159265359 * (radio ** 2))

resultado=area_circulo()
print(resultado)






