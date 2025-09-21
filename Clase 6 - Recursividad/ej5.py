#Calcular la cantidad de dígitos que tiene un número entero.

def digitos(N):
    d=0
    if N<10:
        d=1
    else:
        d=1+digitos(N//10)
        
    return d


print(digitos(141224))