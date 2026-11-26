#crear una funcio para allar si un numero es feliz o no, un numero es feliz si al elevar al cuadrado cada uno de sus digitos y sumarlos se obtiene 1, si no se obtiene 1 se repite el proceso hasta que se obtenga 1 o se caiga en un ciclo infinito
def F_cuadrado(numero):
    suma=0
    i=0
    while numero>0 and suma > 9:
        suma= suma + (numero%10)**2
        numero=numero//10
        i= i+1
    return suma, i

numero = int(input("ingrease el numero que quieras comprovar si es feliz: "))
print(F"el numero al cuadrado es {F_cuadrado(numero)}")
