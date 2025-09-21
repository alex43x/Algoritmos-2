#Dada una lista de números enteros, escribe un programa que encuentre el siguiente número mayor a la derecha de cada elemento. Por ejemplo, si la entrada es [3, 4, 2, 7, 5, 8, 10, 6], la salida debería ser [4, 7, 7, 8, 8, 10, None, None]. El programa debe utilizar una pila para llevar un registro de los elementos aún no procesados.

class Pila():
    def __init__(self):
        self.items=[]
        
    def vacia(self):
        return len(self.items)==0

    def apilar(self,elemento):
        self.items.append(elemento)
    
    def desapilar(self):
        return self.items.pop()
        
    def tope(self):
        return self.items[-1]
    
    def tamano(self):
        return len(self.items)
    
nums=Pila()
L=[4,5,10,4,2,5,9,1]

M=[]

for i in range(len(L)-1,-1,-1):
    nums.apilar(L[i])

n=1
while nums.vacia()!=True and n<len(L):
    vf=False
    i=n
    while i<len(L):
        if L[i]>nums.tope() :
            M.append(L[i])
            nums.desapilar()
            i=len(L)
            vf=True
        else:
            i+=1
            
    if not vf:
        M.append(None)
        nums.desapilar()
    n+=1
    
print(nums.items,M)   