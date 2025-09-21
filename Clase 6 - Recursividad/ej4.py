#Hallar el menor valor de una lista.

L=[4,3,7,2,9,1,6]

def menor(L):
    N=len(L)
    m=L[N-1]
    if N==1:
        m=L[0]
    elif N==2:
        if L[0]<L[1]:
            m=L[0]
        else:
            m=L[1]
    else:
        if menor(L[0:N-1])<m:
            
            m=menor(L[0:N-1])
            print(m,L[0:N-1])
            
            
    print(m)
    return m

menor(L)