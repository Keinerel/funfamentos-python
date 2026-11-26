def capicua(num):
    n = num 
    i = 0
    while (num>0):
        dij = num % 10
        num = num // 10 
        res = i*10+dij
    if (i==n):
        return 1
    else:
        return 0
#prueba
num = int(input("ingresa numero"))
res = capicua(num) 
if res == num :
    print ("tu numero es capicua")
else:
    print("no lo es pa")