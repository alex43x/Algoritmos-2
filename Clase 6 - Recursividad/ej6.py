#Hallar la representación binaria de un número entero y positivo N.

def a_binario(N):
    bin=""
    if N<2:
        return "1"
    else:
        return a_binario(N//2)+str(N%2)
    
print(a_binario(64))