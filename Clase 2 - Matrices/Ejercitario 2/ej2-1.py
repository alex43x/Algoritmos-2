#Verificar si una matriz corresponde a una tabla de sudoku valida
#Comience indicando las propiedades que se cumplen en la matriz del ejemplo y luego escriba un programa Python que reciba una matriz MAT numérica de 9x9 y verifique si su contenido corresponde a un tablero de sudoku correctamente construido. El programa deberá responder: “sudoku correcto” o, en caso contrario, indicar la posición de al menos un valor incorrecto dentro de la matriz.
from matrices import *

def verificar_validez(V):
    print("Numeros" ,V)
    for i in range(9):
        if V[i]==0:
            return [0,i+1,"f"]
        elif V[i]==2:
            return [0,i+1,"s"] 
    return [1]

MAT = [
    [5,3,4,6,7,8,9,1,2],
    [6,7,2,1,9,5,3,4,8],
    [1,9,8,3,4,2,5,6,7],
    [8,5,9,7,6,1,4,2,3],
    [4,2,6,8,5,3,7,9,1],
    [7,1,3,9,2,4,8,5,6],
    [9,6,1,5,3,7,2,8,4],
    [2,8,7,4,1,9,6,3,4],  # duplicado en subgrupo inferior-derecho
    [3,4,5,2,8,6,1,7,9]
]

print("Matriz")
imprimat(MAT)

#Lista para verificar
V=[0]*9

valid=1
i=0

#Verificacion horizontal
while valid==1 and i!=9:
    for j in range(9):
        V[MAT[i][j]-1]+=1
    verif=verificar_validez(V)
    if verif[0]==0:
        if verif[2]=="f":
            print(f"Error: falta el {verificar_validez(V)[1]} en la fila {i}")
        elif verif[2]=="s":
            print(f"Error: hay mas de un {verificar_validez(V)[1]} en la fila {i}")
            
        valid=0
    V=[0]*9
    i+=1
 
 
#Verificacion Vertical
V=[0]*9    
i=0
while valid==1 and i!=9:
    for j in range(9):
        V[MAT[j][i]-1]+=1
    verif=verificar_validez(V)
    if verif[0]==0:
        if verif[2]=="f":
            print(f"Error: falta el {verificar_validez(V)[1]} en la columnas {i}")
        elif verif[2]=="s":
            print(f"Error: hay mas de un {verificar_validez(V)[1]} en la columna {i}")  
        valid=0
    V=[0]*9
    i+=1


# Verificación de subgrupos
k = 0
while valid == 1 and k != 3:
    l = 0
    while valid == 1 and l != 3:
        V = [0]*9
        for i in range(3):
            for j in range(3):
                V[MAT[k*3 + i][l*3 + j] - 1] += 1

        verif = verificar_validez(V)
        if verif[0] == 0:
            if verif[2] == "f":
                print(f"Error: falta el {verif[1]} en el subgrupo ({k},{l})")
            elif verif[2] == "s":
                print(f"Error: hay más de un {verif[1]} en el subgrupo ({k},{l})")
            valid = 0
        l += 1
    k += 1

 
  


if valid==0:
    print("Sudoku invalido")
else:
    print("Sudoku valido")   