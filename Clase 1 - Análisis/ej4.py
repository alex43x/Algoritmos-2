#Hallar la fracción suma entre dos fracciona a/B y c/d

#Analisis
#Se debe pedir el numerador y denaminador de ambas fracciones pro separado

#Solucion 
#La fracción suma será igual a (a.d + b.c)/b.d

print("***Calculo de suma de fracciones***")
a=int(input("Ingrese a "))
b=int(input("Ingrese b "))
c=int(input("Ingrese c "))
d=int(input("Ingrese d "))

while a<1:
    print("El nro debe ser mayor o igual a 1")
    a=int(input("Ingrese a"))

while b<1:
    print("El nro debe ser mayor o igual a 1")
    b=int(input("Ingrese b"))

while c<1:
    print("El nro debe ser mayor o igual a 1")
    c=int(input("Ingrese c"))

while d<1:
    print("El nro debe ser mayor o igual a 1")
    d=int(input("Ingrese d"))

print("La fracción resultante es: ", (a*d + b*c),"/",b*d)