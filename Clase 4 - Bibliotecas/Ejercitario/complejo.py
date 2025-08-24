#Escribir un módulo “complejos.py” para implementar un tipo de datos adecuado para representar números complejos de la forma A + Bi y realizar las siguientes operaciones con ellos: suma, resta, multiplicación, división y potenciación entera.

class Complejo:
    def __init__(self,real,imag):
        self.real=real
        self.imag=imag
    
    def sumar(self,other):
        print(f"La suma es igual a: {self.real+other.real}+{self.imag+other.imag}i")
        
    def restar(self,other):
        print(f"La suma es igual a: {self.real-other.real}+{self.imag-other.imag}i")
        
    def multiplicar(self,other):
        real=self.real*other.real-self.imag*other.imag
        imag=self.real*other.imag+self.imag*other.real
        print(f"La multiplicacion es igual a: {real}+{imag}i")
        m=Complejo(real,imag)
        return m
        
    def dividir(self,other):
        real=(self.real*other.real+self.imag*other.imag)/(other.real**2+other.imag**2)
        imag=(self.imag*other.real-self.real*other.imag)/(other.real**2+other.imag**2)
        print(f"La división es igual a: {real}+{imag}i")
        
    def potencia(self,pow):
        a=self
        for i in range(1,pow):
            a=a.multiplicar(self)
        print(f"Potencia igual a {a.real}+{a.imag}i")
        return a
    
a=Complejo(2,5)
a.potencia(3)
    