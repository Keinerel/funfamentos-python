
#para sacar el factorial de un numero se debe usar un ciclo repetitivo, en este caso se usara why

def f_factorial(n):
    factorial=1
    while n>1:
        factorial = n*factorial
        n = factorial-1
    return factorial


n= int(input("Ingrese un numero para calcular su factorial: "))
print(f"El factorial de {n} es: {f_factorial(n)}")  
