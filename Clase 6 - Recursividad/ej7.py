#Calcular el máximo común divisor de A y B.

def mcd(a,b):
    r=a%b
    if r==0:
        return b
    else:
        return mcd(b,r)
    
print(mcd(30,100))