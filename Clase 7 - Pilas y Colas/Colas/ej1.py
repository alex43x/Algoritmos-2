#1. Dada una lista de números enteros y un número entero k, escribe un programa que encuentre los k elementos más grandes de la lista. El programa debe utilizar una cola de tamaño k para mantener los elementos más grandes encontrados hasta el momento.

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
    
def mayor_k(L,k):
    M=Cola()
    for i in range(k):
        may=L[0]
        for j in range(len(L)):
            if L[j]>may:
                may=L[j]
        M.agregar(may)
        L.remove(may)
    return(M.items)
            
    
L=[3,6,2,9,8,5,8]

k=3 

print(mayor_k(L,k))


    
