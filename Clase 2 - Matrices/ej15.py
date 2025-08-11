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

sum1=0
sum2=0
for i in range(N):
    for j in range(N):
        if i==0 or i==N-1 or j==0 or j==N-1:
            sum1+=M[i][j]
        else:
            sum2+=M[i][j]

            
print("Suma: ",sum1)
print("Suma: ",sum2)


