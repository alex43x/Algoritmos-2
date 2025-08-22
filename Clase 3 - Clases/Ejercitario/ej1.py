#Dadas tres rectas R1, R2 y R3 que forman los lados de un triángulo, calcular la distancia
# “DIST” entre el centro de la circunferencia circunscripta en el triángulo y el origen de coordenadas.
#Asumir que los datos que definen las 3 rectas serán siempre adecuados para el problema y 
# que para todas ellas: a<>0, b<>0 y c<>0.

class Punto2D:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def distancia(self,other):
        distancia=((self.x-other.x)**2+(self.y-other.y)**2)**0.5
        return distancia
    
    def origen(self):
        distancia=(self.x**2+self.y**2)**0.5
        print(f"La distancia al origen es de: {distancia}")
        
    def punto_medio(self,other):
        x=(self.x+other.x)/2
        y=(self.y+other.y)/2
        pm=Punto2D(x,y)
        return pm
        
    def pendiente(self,other):
        m=(self.y-other.y)/(self.x-other.x)
        return m
    
    def mediatriz(self,other):
        pm=self.punto_medio(other)
        m=-1/self.pendiente(other)
        rm=Recta(m,-1,pm.y-m*pm.x)
        return rm
    
    def imprimir(self):
        print(f"({self.x},{self.y})")
        
class Recta:
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
    
    def interseccion(self,other):
        x=(other.b*self.c-self.b*other.c)/(other.a*self.b-self.a*other.b)
        y=(-self.c-self.a*x)/self.b
        pi=Punto2D(x,y)
        return pi
    
    def imprimir(self):
        print(f"{self.a}x, {self.b}y, {self.c}")
    
r1=Recta(4,2,5)
r2=Recta(9,2,1)
r3=Recta(1,7,6)
p1=r1.interseccion(r2)
p2=r1.interseccion(r3)
p3=r2.interseccion(r3)

p1.imprimir()
p2.imprimir()
p3.imprimir()
print()

m1=p1.mediatriz(p2)
m2=p1.mediatriz(p3)

m1.imprimir()
m2.imprimir()

centro=m1.interseccion(m2)
centro.imprimir()

centro.origen()       

        
        
