#Representacion matricial de un Arbol TAA(2015)

from random import randint

class Nodo:
    def __init__(self, valor):
        self.valor=valor
        self.izq=None
        self.der=None  
        
class BST:
    def __init__(self):
        self.raiz=None
        self.matriz=[]
        self.n=1
        
        
        
    def agregar(self, valor):
        if self.raiz is None:
            self.raiz=Nodo(valor)
            self.matriz.append([self.n,0,valor,0])
            self.n+=1
        else:
            self._agregar(valor,self.raiz)
    
    def _agregar(self,valor,nodo_actual):
        if valor<nodo_actual.valor:
            if nodo_actual.izq is None:
                nodo_actual.izq=Nodo(valor)
                self.matriz.append([self.n,0,valor,0])
                idx=self.buscar(nodo_actual.valor)
                self.matriz[idx][1]=self.n
                self.n+=1
            else:
                self._agregar(valor,nodo_actual.izq)
        else:
            if nodo_actual.der is None:
                nodo_actual.der=Nodo(valor)
                self.matriz.append([self.n,0,valor,0])
                idx=self.buscar(nodo_actual.valor)
                self.matriz[idx][3]=self.n
                self.n+=1
            else:
                self._agregar(valor,nodo_actual.der)
    
    def buscar(self,valor):
        for i in range(len(self.matriz)):
            if valor ==self.matriz[i][2]:
                return i
    
    def mostrar_arbol(self, nodo=None, nivel=0):
        if nodo is None:
            nodo = self.raiz
        
        if nodo is None:
            return
        
        print("  " * nivel + f"({nodo.valor})")
        
        if nodo.izq:
            self.mostrar_arbol(nodo.izq, nivel + 1)
        if nodo.der:
            self.mostrar_arbol(nodo.der, nivel + 1)
        
                
L=[]
N=int(input("Ingrese valor de N "))
for i in range(2**N-1):
    valid=0
    while valid==0:
        val=randint(1,99)
        if val not in L:
            valid=1
            L.append(val)
            
            
L.sort()
print(L)
Arbol=BST()         
            
def insert(L):
    m=len(L)//2
    if len(L)==1:
        Arbol.agregar(L[0])
    else:
        
        Arbol.agregar(L[m])
        insert(L[:m])
        insert(L[m+1:])
insert(L)

Arbol.mostrar_arbol()

print(Arbol.matriz)