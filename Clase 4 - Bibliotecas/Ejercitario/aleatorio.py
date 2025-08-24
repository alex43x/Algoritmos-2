#Suponiendo que solo se dispone de la función random(), que genera un valor real pseudo aleatorio X (0.0 >= X < 1.0), construir el módulo “aleatorio.py” para implementar las siguientes funciones:

from random import random

def azarent(A,B):
    a=True
    rn=int(B+(A+1-B)*random())
    return rn

def azarele(L):
    n=len(L)
    return L[azarent(n-1,0)]

def azarmes(L):
    M=[0]*len(L)
    n=0
    for c in range(len(M)):
        e=True
        while e==True:
            e=False
            n=azarent(len(L)-1,0)
            print(n)
            for i in range(len(L)):
                if(L[n]==M[i]):
                    e=True
        M[c]=L[n]
    return M

def azarlis(N):
    if N >=1000:
        return
    M=[-1]*N
    for c in range(N):
        e=True
        while e==True:
            e=False
            a=azarent(999,0)
            
            for i in range(N):
                if(a==M[i]):
                    e=True
        M[c]=a  
          
    print(M)
    
def azarmue(L,P):
    n=int(len(L)*P/(100))
    
    M=[0]*n
    for c in range(n):
        e=True
        while e==True:
            e=False
            n=azarent(len(L)-1,0)
            print(n)
            for i in range(len(M)):
                if(L[n]==M[i]):
                    e=True
        M[c]=L[n]
    return M

        
        
        