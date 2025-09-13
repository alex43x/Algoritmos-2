#Se solicita redactar un algoritmo en Python que reciba la matriz creada en el PASO 2 y obtenga e imprima la matriz resultante del PASO 3.   
from matrices import *
def colocar(DIC,PALABRAS):
    for i in range(10):
        valid=0
        cw=0
        word=""
        x,y=PALABRAS[i][0],PALABRAS[i][1]
        while valid==0 and cw<19:
            valid=1
            if len(DIC[cw])==PALABRAS[i][2]:
                word=DIC[cw]
                for k in range(len(word)):
                    
                    if PALABRAS[i][3]=="H" and (A[x][y+k]!=1 and word[k]!=A[x][y+k]):
                        valid=0
                    if PALABRAS[i][3]=="V" and (A[x+k][y]!=1 and word[k]!=A[x+k][y]):
                        valid=0
                    
            else:
                valid=0
                word=""
            cw+=1
        if PALABRAS[i][3]=="H":        
            for k in range(len(word)):
                    A[x][y+k]=word[k]
        else:
            for k in range(len(word)):
                    A[x+k][y]=word[k]
        print()
        imprimat(A)           
            


A=[[1,1,1,0,0,0,1,1,1,1],
   [1,0,0,0,0,0,0,0,0,1],
   [1,0,0,0,1,0,0,0,0,1],
   [1,0,0,0,1,1,1,1,1,1],
   [1,0,0,0,1,0,0,0,0,0],
   [1,0,0,0,1,0,1,1,1,1],
   [1,0,0,0,1,0,0,0,0,0],
   [0,0,1,0,0,1,0,0,0,0],
   [0,0,1,0,0,1,0,0,0,0],
   [0,0,1,0,0,1,1,1,1,1]]

DIC = [
    "SOL",       # 3 letras
    "CASA",      # 4 letras
    "PERRO",     # 5 letras
    "LUNA",      # 4 letras
    "NUBE",      # 4 letras
    "ARBOL",     # 5 letras
    "RANA",      # 4 letras
    "CIELO",     # 5 letras
    "JUEZ",      # 4 letras
    "AVE",       # 3 letras
    "GOL",       # 3 letras
    "PROGRAMAR", # 9 letras
    "AMIGOS",    # 6 letras (por si aparece vertical de 6)
    "ESTUDIOS",  # 8 letras
    "MATICES",   # 7 letras
    "VA",        # 2 letras
    "NO",
    "REMOS",
    "SABRASS"# 2 letras
]
PALABRAS=[0]*10

#Barrido horizontal
cw=0
for i in range(10):
    for j in range(9):
        if A[i][j]==1 and A[i][j-1]==0 or (j==0 and A[i][j]==1 ):
            n=0
            while j+n<10 and A[i][j+n]==1 :
                n+=1
            if n>1:
                PALABRAS[cw]=[i,j,n,"H"]
               
                cw+=1
#Barrido Vertical
for j in range(10):
    for i in range(9):
        if A[i][j]==1 and A[i-1][j]==0 or (i==0 and A[i][j]==1 ):
            n=0
            while i+n<10 and A[i+n][j]==1 :
                n+=1
            if n>1:
                PALABRAS[cw]=[i,j,n,"V"]
                
                cw+=1
                
colocar(DIC,PALABRAS)
            

            
        
            
            

   