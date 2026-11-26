#numero invertido sin importar las cifras que tenga el numero
def f_invertir(numero):
    invertido=0
    while numero>0:
        invertido= invertido*10 + numero%10
        numero=numero//10
    return invertido

#principal
numero= int(input("Ingrese el numero a invertir: "))
invertido= f_invertir(numero)
print(f"El numero invertido de {numero} es: {invertido}")
