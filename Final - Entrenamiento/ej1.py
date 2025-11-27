#Un bolillero contiene 100 bolillas numeradas del 1 al 100.
# Del bolillero se extraen 40 bolillas y se colocan en la matriz CUADRO de 8 filas y 5 columnas.
# ¿Cuál es la probabilidad de que los elementos de una de sus columnas sumen igual que los elementos de una de sus filas? Escribir un programa Python que repita este experimento N veces y calcule la probabilidad buscada. El valor N debe ser ingresado por el usuario 

import random
from matrices import *

N=int(input("Ingrese cantidad de repeticiones del experimento "))

def check_sumas(Cuadro):
    sf=[]
    sc=[0]*5
    for i in range(8):
        sf.append(sum(Cuadro[i]))
    for i in range(8):
        for j in range(5):
            sc[j]+=Cuadro[i][j]

    for i in range(5):
        if sc[i] in sf:
            return True
    
    return False       

def experimento():
    Cuadro=creamat(8,5)
    Bol=[]

    for i in range(100):
        Bol.append(i+1)
        
    for i in range(8):
        for j in range(5):
            a=random.choice(Bol)
            Bol.remove(a)
            Cuadro[i][j]=a
    
    if check_sumas(Cuadro)==True:
        imprimat(Cuadro)
        return True
    return False

c=0
for i in range(N):
    if experimento()==True:
        c+=1
        print(1)
    print(i)

print(f"Probabilidad: {c*100/N}%")       