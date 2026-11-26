def menu():
    """
    1-Seno
    2-coseno
    3-salir perro
    """

def f_potencia( base, exponente):
    pot=1
    i=1
    while i<=exponente:
        pot=pot*base
        i=i+1
    return pot

def f_factorial(numero):
    factorial=1
    for i in range(1, numero + 1):
        factorial=factorial* i
    return factorial

for x in range(1,15+1,2):
    