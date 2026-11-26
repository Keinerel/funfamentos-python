def factorion(numero):
    acumulador = 1 
    contador = numero
    dup = numero
    while (numero > 0):
        acumulador = (contador * (numero-1))
        numero = numero -1
        contador = contador - 1
    return acumulador



# prueba 

numero = int(input("ingrese numero"))
print (f"su resultado es: {factorion(numero)}")
