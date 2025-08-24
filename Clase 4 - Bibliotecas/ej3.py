#Preparar un programa que utilice el módulo “itertools” para generar las combinaciones de N elementos tomados de P en P.

from itertools import combinations

n=int(input("Ingrese valor de N"))
p=int(input("Ingrese valor de P"))


r=[0]*n
for i in range(n):
    r[i]=int(input("Ingrese valor para r"))

c=combinations(r,p)


print(f"Combinaciones posibles: {list(c)}")