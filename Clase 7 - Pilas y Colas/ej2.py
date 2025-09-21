#Dado un número entero, escribe una función que lo convierta a su representación en binario utilizando una pila.

class Pila():
    def __init__(self):
        self.items=[]
        
    def vacia(self):
        return len(self.items)==0

    def apilar(self,elemento):
        self.items.append(elemento)
    
    def desapilar(self):
        self.items.pop()
        
    def tope(self):
        return self.items[-1]
    
    def tamano(self):
        return len(self.items)
    
def a_binario(n):
    ds=Pila()
    while n//2>=2:
        n,b=n//2,n%2
        ds.apilar(b)
    ds.apilar(n//2)
    ds.items.reverse()
    return ds.items
    
print(a_binario(72))
    
    
    