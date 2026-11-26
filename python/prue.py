def menu():
    print('''
    _____________________________
   |tipo de automotor |  costo   |
   |1.vehículo        |  $3.500  |
   |2.Camión          |  $12.000 |
   |3.Tractomula      |  $16.300 |
   |-----------------------------|
   |0. salir del programa        |
    =============================
''')

def valorind(tipovehi):
    tip1 = 0
    tip2 = 0
    tip3 = 0
    if tipovehi == 1 :
        cost = 3500
        tip1 = tip1 + 1
    elif tipovehi == 2 :
        cost = 12000
        tip2 = tip2 +1
    elif tipovehi == 3 :
        cost = 16300
        tip3 = tip3 + 1
    return cost, tip1, tip2, tip3

def totalporvehi():
    _, tip1, tip2, tip3 = valorind()
    t1 = tip1 * 3500
    t2 = tip2 * 12000
    t3 = tip3 * 16300
    total = t1 + t2 + t3
    return t1, t2, t3, total

def vehimayor():
    _, tip1, tip2, tip3 = valorind
    mayor = max (tip1,tip2,tip3)
    return mayor


#cree la funcion principal que muestre menu y solicite el tipo de automotor al usuario, luego llame a la funcion valorind y muestre el costo del automotor seleccionado y que al oprimir 0 muestre el total de cada tipo de automotor y el total general de todos los automotores ingresados, ademas de mostrar cual fue el tipo de automotor que mas se ingreso.
menu()
tipovehi = int(input("Ingrese el tipo de automotor (1, 2, 3) o 0 para salir: "))
while tipovehi != 0:
    cost, tip1, tip2, tip3 = valorind(tipovehi)
    print(f"El costo del automotor seleccionado es: ${cost}")
    menu()
    tipovehi = int(input("Ingrese el tipo de automotor (1, 2, 3) o 0 para salir: "))
    if tipovehi == 0:
        t1, t2, t3, total = totalporvehi()
        print(f"Total de vehículos: ${t1}")
        print(f"Total de camiones: ${t2}")
        print(f"Total de tractomulas: ${t3}")
        print(f"Total general: ${total}")
        mayor = vehimayor()
        if mayor == tip1:
            print("El tipo de automotor que más se ingresó fue: Vehículo")
        elif mayor == tip2:
            print("El tipo de automotor que más se ingresó fue: Camión")
        elif mayor == tip3:
            print("El tipo de automotor que más se ingresó fue: Tractomula")
        
