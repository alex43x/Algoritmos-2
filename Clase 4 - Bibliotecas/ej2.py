#Preparar un programa que utilice el módulo “math” para calcular la cantidad de combinaciones de N elementos tomados de P en P.


from math import comb

n=int(input("Ingrese valor de N"))
p=int(input("Ingrese valor de P"))

c=comb(n,p)

print(f"Combinaciones posibles: {c}")
