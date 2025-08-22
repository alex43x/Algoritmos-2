#Clase rectangulo con atributos largo y ancho y metodos area y perimetro

class Rectangulo:
    def __init__(self, largo, ancho):
        self.largo=largo
        self.ancho=ancho
    
    def perimetro(self):
        print(f"Perimetro: {2*(self.ancho+self.largo)} u")
        
    def area(self):
        print(f"Area: {self.largo*self.ancho} u2")
        
r1=Rectangulo(4,5)
r1.area()
r1.perimetro()