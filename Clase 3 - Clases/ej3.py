#Clase Punto2d con atributos de coordenada y metodos de distancia entre si y distancia al origen de coordenadas

class Punto2D:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def distancia(self,other):
        distancia=((self.x-other.x)**2+(self.y-other.y)**2)**0.5
        print(f"La distandcia entre los puntos es de {distancia}")
    
    def origen(self):
        distancia=(self.x**2+self.y**2)**0.5
        print(f"La distancia al origen es de: {distancia}")
        
p1=Punto2D(3,4)
p2=Punto2D(0,4)
p1.distancia(p2)
p1.origen()