#Su aporte consiste en programar los siguientes elementos para la aplicación:
# 1- Una función crearbol() que recibe la cantidad de nodos y permite ingresar el árbol.
# 2- Una función sumarbol() que recibe el árbol y un código de nodo y retorna la suma de los valores de todos los descendientes de ese nodo.
# 3- Una función binarbol() que recibe el árbol y retorna 1 si el mismo es binario y 0 en caso contrario.
# 4- Una función hojarbol() que recibe el árbol e imprime la lista de las hojas del árbol.

from matrices import *

def search(v,L):
    for i in range(len(L)):
        if L[i][0]==v:
            return i+1
        
    return 0

def crearbol(N):
    A1=creamat(N,3)
    for i in range(N):
            A1[i][0]=str(input(f"Ingrese código del Nodo {i+1}: "))
            A1[i][1]=int(input(f"Ingrese valor del Nodo {i+1}: "))
    
    print("Ingrese las relaciones")        
    for i in range(N):
        n=input(f"Ingrese padre del nodo {A1[i][0]}: ")
        A1[i][2]=search(n,A1)
    
    return A1,sumarbol(A1,"f")

def sumarbol(A1,N):
    s=0
    print(N,A1,s)
    for i in range(len(A1)):
        if A1[i][0]==N:
            p=i
    for i in range(len(A1)):
        if A1[i][2]==p+1:
            s=s+A1[i][1]+sumarbol(A1,A1[i][0])
    return s  

def inicio(A1):
    for i in range(len(A1)):
        if A1[i][2]==0:
            return A1[i][0] 
    
def binarbol(A1,N):
    c=0
    for i in range(len(A1)):
        if A1[i][0]==N:
            p=i
            
    for i in range(len(A1)):
        if A1[i][2]==p+1:
            if binarbol(A1,A1[i][0])==0:
                return 0
            else:
                c+=1
    if c>2:
        return 0
    return 1    
        
def hojarbol(A1,N):
    c=0
    hojas=[]
    for i in range(len(A1)):
        if A1[i][0]==N:
            p=i
    
    for i in range(len(A1)):
        if A1[i][2]==p+1:
            h=hojarbol(A1,A1[i][0])
            hojas.append(h)
            c+=1
    if c==0:
        return N
    return hojas       
    


A1=[["a",1,2],
    ["b",3,3],
    ["c",5,5],
    ["d",7,0],
    ["e",9,4],
    ["f",9,4]]      

print(sumarbol(A1,"c"))
print(binarbol(A1,inicio(A1)))
print(hojarbol(A1,inicio(A1)))


            