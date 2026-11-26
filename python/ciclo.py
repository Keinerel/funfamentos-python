


#para sacar el factorial de un numero se debe usar un ciclo repetitivo, en este caso se usara for


def f_factorial(numero):
    factorial=1
    for i in range(1, numero + 1):
        factorial=factorial* i
    return factorial

numero= int(input('Ingrese un numero para calcular su factorial: '))
resultado= f_factorial(numero)
n = numero / 2 
print('El factorial de', numero, 'es:', resultado)
