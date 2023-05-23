def resta (a, b):
    #print (a-b)
    #en lugar de print DEVOLVER usando return
    return a-b

resultado=resta(5, 2)
print(resultado)


def pares (numero):
   # print (numero % 2 == 0)
    return numero % 2 == 0

resultado=pares (7)
print(resultado)


def es_bisiesto(anio):
   # print (anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0))
    return  (anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0))

resultado=es_bisiesto(2016)
print(resultado)


def convertir_mayusculas(cadena):
    #print (cadena.upper())
    return cadena.upper()

resultado=convertir_mayusculas("meliana")
print(resultado)


def verificar_signo(numero):
    if numero > 0:
       # print ("Positivo")
        return "Positivo"
    elif numero < 0:
        #print ("Negativo")
        return "Negativo"
    else:
       # print ("Cero")
       return "Cero"

resultado=verificar_signo(-8)
print(resultado)
