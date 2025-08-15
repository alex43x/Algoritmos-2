#Su equipo de desarrollo de software está encargado de la programación de un juego conocido como Batalla Naval. El juego se desarrolla sobre un tablero que se representa mediante una matriz de 10 filas y 10 columnas, llamada TAB, en la cual inicialmente todos los elementos valen cero (0). 
# Sobre esta matriz deben colocarse aleatoriamente los siguientes barcos: 2 barcos de tamaño 5, 2 barcos de tamaño 4 y 3 barcos de tamaño 3. Cada barco se representa mediante celdas con valor uno (1) y puede colocarse horizontal o verticalmente.
# Su trabajo, como parte del equipo, consiste en escribir una función que reciba la matriz TAB vacía y la modifique para incluir los barcos, sabiendo que cada barco no puede tocarse en ningún punto con los demás barcos.
# Al concluir, se deberá imprimir la matriz TAB resultante. 

from matrices import *
from random import randint

TAB=creamat(10,10)
imprimat(TAB)

def revisar_espacio(x,y,ot,long):
    if ot==1:           #si es vertical
        for i in range(-1,long):
            print(TAB[x+i][y])
            if y!=0 and y!=9:
                if TAB[x+i][y]!=0 or TAB[x+i][y-1]!=0 or TAB[x+i][y+1]!=0:
                    return 0
            elif y==0:
                if TAB[x+i][y]!=0 or TAB[x+i][y+1]!=0:
                    return 0
            else:
                if TAB[x+i][y]!=0 or TAB[x+i][y-1]!=0:
                    return 0
    else:               #si es horizontal
        for i in range(-1,long):
            if x!=0 and x!=9:
                if TAB[x][y+i]!=0 or TAB[x-1][y+i]!=0 or TAB[x+1][y+i]!=0:
                    return 0
            elif x==0:
                if TAB[x][y+i]!=0 or TAB[x+1][y+i]!=0:
                    return 0
            else:
                if TAB[x][y+i]!=0 or TAB[x-1][y+i]!=0:
                    return 0
    print("Valido")
    return 1
    

def colocar_barco(long):
    valid=0
    while valid==0: #Repite hasta que aparezca una ubicación valida
        ot=randint(1,2) #Orientación de los barcos, 1-vertical,2-horizontal
        if ot==1:
            x=randint(0,10-long)
            y=randint(0,9) #Genera una coordenada aleatoria
        else:
            x=randint(0,9)
            y=randint(0,10-long) #Genera una coordenada aleatoria
        valid=revisar_espacio(x,y,ot,long)
        print(x,y,ot,long)
    
    if ot==1:           #si es vertical
        for i in range(long):
            TAB[x+i][y]=1
    else:               #si es horizontal
        for i in range(long):
            TAB[x][y+i]=1
    print("Barco colocado")
    imprimat(TAB)
    
revisar_espacio(3,2,1,5)  
colocar_barco(3)
colocar_barco(3)
colocar_barco(3)
colocar_barco(4)
colocar_barco(4)
colocar_barco(5)
colocar_barco(5)


    
    