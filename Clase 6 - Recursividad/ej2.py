#Encontrar el valor del enésimo número de la serie de Fibonacci.

def fibonacci(N):
    if N==0:
        f=0
    elif N==1:
        f=1
    else:
        f=fibonacci(N-2)+fibonacci(N-1)
    return f
        
print(fibonacci(6))
        