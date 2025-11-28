"""Listas y Sub listas TAA(2018)"""

from random import *

def ordena_sub(V,P):
    cortes=[]
    N=len(V)
    r=N//P
    
    for i in range(P-1):
        cortes.append(r*(i+1))
    print(cortes)
    
    L=[V[0:cortes[0]]]
    for i in range(0,len(cortes)-1):
        L.append(V[cortes[i]:cortes[i+1]])
    L.append(V[cortes[len(cortes)-1]:])
    print(V)
    print(L)    
    
    for i in range(len(L)):
        L[i].sort()
    return L   
        
def combina_sub(V,P):
    L=[]
    opciones=[]
    total=0
    for i in range(P):
        total+=len(V[i])
        opciones.append(V[i][0])
    
    print(V)
    while total>0:
        L.append(min(opciones))
        faltante=opciones.index(min(opciones))
        if len(V[faltante])>0:
            V[faltante].pop(0)
        
        if len(V[faltante])>0:
            opciones[faltante]=V[faltante][0]
        
        
        
        print(total,L,V,opciones)
            
        total-=1
    print(L)
        


N=20
P=3

L=[]
for i in range(N):
    n=randint(1,10)
    L.append(n)
    
V=ordena_sub(L,P)
combina_sub(V,P)
L.sort()
print(L)  

