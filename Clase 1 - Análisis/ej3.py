#Determinar factores primos comunes entre dos nros A y B

#Análisis
# Se debe atender que los nros ingresados sean mayores a 1, de modo que sea posible la aplicación de la descomposicion de numeros en sus factores primos

#Solución
# Aplicar euclides para obtener el mcd y luego descomponerlo, ya que el mcd esta formado por los factores comunes de ambos nros

def mcd(a,b):
    while b!=0:
        a,b=b,a%b
    return a

def obtener_primo(ultpr):
    fc=1
    while fc!=2:
        ultpr+=1
        fc=1
        for i in range(2, ultpr+1):
            if ultpr%i==0:
                fc+=1
    return ultpr

print("***Calculo de Factores comunes***")
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

pr=2
mcd=mcd(n1,n2)
print("***Primos comunes***")
while (mcd!=1):
    while mcd%pr==0:
        mcd=mcd/pr
    print(pr,end=", ")
    pr=obtener_primo(pr)
    
        