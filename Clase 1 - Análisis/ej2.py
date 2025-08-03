#Hallar el MCM entre dos nros

#Análisis 
# Se debe atender que los nros ingresados sean mayores a 1, de modo que sea posible aplicarles el algoritmo de euclides

# - Solución
#Se utilizara el algoritmo de euclides, que se utiliza para calcular mcd, luego se utilizara la propiedad de que mcm(a,b)=a.b/mcd(a,b)

def mcd(a,b):
    while b!=0:
        a,b=b,a%b
    return a


print("***Calculo de MCM***")
n1=int(input("Ingrese el primer nro"))
n2=int(input("Ingrese el segundo nro"))

while n1<2:
    print("El nro debe ser mayor a 1")
    n1=int(input("Ingrese el primer nro"))

while n2<2:
    print("El nro debe ser mayor a 1")
    n2=int(input("Ingrese el segundo nro"))

if n1<n2:
    n1,n2=n2,n1

print("El MCM es: ", int((n1*n2)/mcd(n1,n2)))


