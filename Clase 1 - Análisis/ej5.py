#Imprimir todos los valores a,b y c menores a 100 que puedan representar los lados de triangulo rectangulo

#Análisis
#se debe considerar que la suma de los catetos siempre será mayor a la hipotenusa, para evitar ciclos innecesarios

#Solución 
#Con estructuras repetitivas, revisar las combinaciones posibles si cumplen, valiendonos del teorema de pitagoras

def buscar_triangulos(max):
    for a in range(1,max):
        for b in range(a+1,max):
            c=(a**2+b**2)**0.5
            if c.is_integer() and c<max:
                print(a,b,int(c),sep=", ")

buscar_triangulos(100)         


