#Dado un número entero, escribe un programa que encuentre los números primos menores o iguales a él. El programa debe utilizar una cola para almacenar los números pendientes de procesar.

class Cola():
    def __init__(self):
        self.items=[]
    
    def vacia(self):
        return len(self.items)==0
    
    def agregar(self,elemento):
        self.items.append(elemento)
    
    def sacar(self):
        return self.items.pop(0)
    
    def tamano(self):
        return len(self.items)
    
def primos(N):
    pendiente=Cola()
    ps=[]
    for i in range(2,N+1):
        pendiente.agregar(i)
    
    while pendiente.vacia()==False:
        c=0
        for i in range(1,pendiente.items[0]+1):
            if pendiente.items[0]%i==0:
                c+=1
        if c==2:
            ps.append(pendiente.items[0])
        pendiente.sacar()
        
    return ps

print(primos(10))
        