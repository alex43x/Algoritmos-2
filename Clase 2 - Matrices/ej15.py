#Suma de los bordes de la matriz, y opuesto
N=int(input("Ingrese valor de N "))
M=[]
for i in range(N):
    M.append([])
    for j in range(N):
        M[i].append([])
        M[i][j]=int(input("Ingrese un valor "))
        
for i in range(N):
    print(M[i])

sumas=[0]*8
for i in range(N):
    for j in range(N):
        if i==0 or i==N-1 or j==0 or j==N-1:
            sumas[0]+=M[i][j]
        else:
            sumas[1]=M[i][j]

for i in range(N):
    for j in range(N):
        if i!=round(N/2)-1 and j!=round(N/2)-1:
            sumas[2]+=M[i][j]

for i in range(N):
    for j in range(N):
        if i+j<N-1:
            sumas[3]+=M[i][j]
            
for i in range(N):
    for j in range(N):
        if i+j<N-1 and j>i:
            sumas[4]+=M[i][j]
 
for i in range(N):
    for j in range(N):
        if i+j>N-1 and j>i:
            sumas[5]+=M[i][j]
            
for i in range(N):
    for j in range(N):
        if i+j>=N-1:
            sumas[6]+=M[i][j]
            
for i in range(N):
    for j in range(N):
        if i%2==1 or j%2==1:
            sumas[7]+=M[i][j]
            
print("Suma (bordes): ",sumas[0])
print("Suma (interior): ",sumas[1])
print("Suma (cuadros): ",sumas[2])
print("Suma (triangulo 1): ",sumas[3])
print("Suma (triangulo 2)): ",sumas[4])
print("Suma (triangulo 3)): ",sumas[5])
print("Suma (triangulo 4)): ",sumas[6])
print("Suma (cruces)): ",sumas[7])



