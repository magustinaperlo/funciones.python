def saludos ():
    #print ("buen dia")
    return "buen dia"

resultado=saludos()
print(resultado)


def poema ():
     return ("Por más que cante un pájaro en el bosque, el ciruelo no rompe a florecer - Aiku")

resultado= poema()
print(resultado)


def nombre_edad ():
    return(" Meliana, 26 años")

resultado= nombre_edad ()
print(resultado)


def ciudad ():
    return ("Malagueño")

resultado=ciudad()
print(resultado)


def mostrar_numeros_impares():
    impares = []
    for numero in range(1, 21, 2):
        #print(numero)
        impares.append(numero)
     return impares

resultado=mostrar_numeros_impares()
print(resultado)




