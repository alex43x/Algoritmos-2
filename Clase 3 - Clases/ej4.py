#Clase complejo con operaciones aritmeticas basicas

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
        
    def dividir(self,other):
        real=(self.real*other.real+self.imag*other.imag)/(other.real**2+other.imag**2)
        imag=(self.imag*other.real-self.real*other.imag)/(other.real**2+other.imag**2)
        print(f"La división es igual a: {real}+{imag}i")
        
c1=Complejo(6,4)
c2=Complejo(2,3)

c1.sumar(c2)
c1.restar(c2)
c1.multiplicar(c2)
c1.dividir(c2)
        