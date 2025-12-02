"""Usted forma de parte de un grupo de programación que está desarrollando una aplicación
para realizar operaciones con árboles donde cada nodo almacena 2 datos: código (cadena)
y valor (entero). """

def crearbol(N):
    A1=[[0,0,0]]
    for i in range(N):
        cod=str(input("Ingrese codigo: "))
        val=int(input("Ingrese valor: "))
        pad=int(input("Ingrese padre: "))
        A1.append([cod,val,pad])
    return A1

def sumarbol(A1,cod):
    val=0
    for i in range(len(A1)):
        if A1[i][0]==cod:
            idx=i
    print(idx)
    for i in range(len(A1)):
        if idx==A1[i][2]:
            val+=A1[i][1]
            val+=sumarbol(A1,A1[i][0])
    return val

def binarbol(A1):
    c=0
    for i in range(len(A1)):
        for j in range(len(A1)):
            if A1[j][2]==i:
                c+=1
        if c>2:
            return 0
        c=0
    return 1

def hojarbol(A1):
    hojas=[]
    c=0
    for i in range(len(A1)):
        for j in range(len(A1)):
            if i==A1[j][2]:
                c+=1
        if c==0:
            hojas.append(A1[i][0])
        c=0
    return hojas
                
A1=crearbol(7)    
print(A1)
print(sumarbol(A1,"F4"))  
print(binarbol(A1))  
print(hojarbol(A1))  
        