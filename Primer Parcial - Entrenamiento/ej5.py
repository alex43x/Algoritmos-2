#Se pide escribir un algoritmo capaz de generar aleatoriamente una boleta de Bingo que cumpla con las especificaciones señaladas. El algoritmo deberá imprimir la boleta generada.

from matrices import *
from random import randint

B=creamat(3,9)

sf=[0]*3
sc=[0]*9

vf=0

li=[1,10,20,30,40,50,60,70,80]
ls=[9,19,29,39,49,59,69,79,89]


    
sw=-3
for i in range(2):
    for j in range(9): 
          
        if sc[j]==0 and i==2:
            B[i][j]=1
            sf[i]+=1
            sc[j]+=1
        elif sf[i]==5:
            B[i][j]=0
        elif 9-j==5-sf[i]:
            B[i][j]=1
            sf[i]+=1
            sc[j]+=1
        else:
            num=randint(0,1)
            B[i][j]=num
            if num==1:
                sf[i]+=1
                sc[j]+=1
                
for j in range(9):
    
    if sc[j]==0:
        B[2][j]=1
        sc[j]+=1
        sf[2]+=1
for j in range(9):
    if B[2][j]==1:
        pass
    elif sf[2]==5:
            B[2][j]=0
    elif 9-j==5-sf[2]:
            B[2][j]=1
            sf[2]+=1
            sc[j]+=1
    else:
        num=randint(0,1)
        B[2][j]=num
        if num==1:
            sf[2]+=1
            sc[j]+=1
        
for i in range(3):
    for j in range(9):
        vf=0
        while vf==0:
            vf=1
            if B[i][j]==1:
                if li[j]>=ls[j]-i-2:
                    num=li[j]+1
                    li[j]+=1
                else:
                    num=randint(li[j],ls[j]-i-2)
                    
                for k in range(3):
                    if  num == B[k][j]:
                        vf=0
                if vf==1:
                    B[i][j]=num  
                    li[j]=num                


imprimat(B)
