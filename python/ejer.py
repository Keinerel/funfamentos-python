import time

def menu():
    print ('''
     _____________________________
    | Elija que vamos a averigual |
    |-----------------------------|
    | 1.Cubo interesante          |
    | 2.Factorion                 |
    | 3.potenciación              |
    | 4.suma simple               |
    | 5.resta simple              |
    | 6.salir                     |
     =============================

''')
# hacer una funcion para averiguar si un numero es un factorion, un numero es un factorion si la suma de los factoriales de sus digitos es igual al numero original, por ejemplo 145 es un factorion porque 1! + 4! + 5! = 145 
def ffactorion(numero):
    acumulador = 0
    while(numero>0):
        frax = numero%10
        numero = numero // 10 
        factorial = 1
        for i in range(1, frax + 1):
            factorial = factorial * i
        acumulador = acumulador + factorial
    return acumulador

def potencia (base, exponente):
    pot = 1
    i = 1
    while i<=exponente :
        pot = pot * base
        i = i + 1
    return pot 

def suma(n1,n2):
    resultado = n1 + n2
    return resultado

def resta(n1,n2):
    resultado = n1 - n2
    return resultado


def fcubointeresante(numero):
    acumulador = 0
    while(numero>0):
        frax = numero%10
        numero = numero // 10 
        acumulador = acumulador + ((frax*frax)*frax)
    return acumulador

# principal 
while True:
    menu()
    tipo = int(input("igrese que deseas averiguar: "))
    if (tipo == 1):
        numero = int(input("ingrese un numero: "))
        acumulador = fcubointeresante(numero)
        if (acumulador == numero):
            print ("your number is happy")
        else:
            print ("your number is not happy")
        time.sleep(3)
    elif (tipo == 2):
        numero = int(input("ingrese un numero: "))
        acumulador = ffactorion(numero)
        if (acumulador == numero):
            print ("your number is a factorion")
        else:
            print ("your number is not a factorion")
            time.sleep(3)
    elif (tipo == 3):
        base= int(input("Ingrese la base: "))
        exponente= int(input("Ingrese el exponente: "))
        pot = potencia( base , exponente )
        print (f"El numeoro {base} elevado a {exponente} da resultado de {pot}")
        time.sleep(4)    
    elif (tipo == 4):
        n1 = int(input("ingrese el primer numero: "))
        n2 = int(input("ingrese el segundo numero: "))
        res = suma(n1,n2)
        print (f"el resultado de la suma es: {res}")
        time.sleep(3)
    elif (tipo == 5):
        n1 = int(input("ingrese el numero mayor: "))
        n2 = int(input("ingrese el numero menor: "))
        res = resta(n1,n2)
        print(f"el resultado de la resta es: {res}")
        time.sleep(3)
    elif (tipo == 6):
        print ("saliendo del programa")
        time.sleep(1)
        print("saliendo del programa.")
        time.sleep(1)
        print("saliendo del programa..")
        time.sleep(1)
        print("saliendo del programa...")
        time.sleep(1)
        print("saliendo del programa....")
        time.sleep(2)
        print("se salio exitosamente")
        break
        

