def precios():
    print('''
     _______________________________
    |       1.Bogotà  |    2.Cali   |
    |-------------------------------|   
    | 1 clase 250.000 |      450.000|   
    | 2 clase 180.000 |      350.000|
    | 3 clase 150.000 |      300.000|
     ===============================
    ''')


def descuento(numpas):
    if (numpas > 5):
        des= 0.1
    else :
        des= 1
    return des

def total(numpas, des, clase, destino):
    if (clase == 1 and destino == 1):
        total= (250000 * numpas) * des
    elif (clase == 2 and destino == 1):
        total= (180000 * numpas) * des
    elif (clase == 3 and destino == 1):
        total= (150000 * numpas) * des
    elif (clase == 1 and destino == 2):
        total= (450000 * numpas) * des
    elif (clase == 2 and destino == 2):
        total= (350000 * numpas) * des
    elif (clase == 3 and destino == 2):
        total= (300000 * numpas) * des
    return total


print('Bienvenido a la agencia de viajes')
print(precios())
numpas= int(input('Ingrese el numero de pasajeros: '))
des= descuento(numpas)
clase= int(input('Ingrese la clase de viaje: '))
destino= int(input('Ingrese el numero de destino(1 o 2): '))
total= total(numpas, des, clase, destino)
rint('El total a pagar es: ', total)
