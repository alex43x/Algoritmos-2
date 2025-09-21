#Hallar la suma de los N primeros números.

def suma(N):
    if N==1:
        s=1
    else:
        s=N+suma(N-1)
    return s

print(suma(6))