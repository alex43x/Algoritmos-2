#Un tema bien estudiado en matemáticas es el desarrollo de la potencia de un binomio.
# Cuando se eleva el binomio a una potencia n, se genera una expresión de la forma:

#Se pide:
# - Utilizar una estructura de datos adecuada y conveniente para representar un polinomio.
# - construir la función potenciabin( A , N ), que reciba los valores numéricos de a y n y devuelve el polinomio correspondiente al desarrollo de (x + a)n.
# - construir el procedimiento impripol( P ) que recibe un dato de tipo p

class Polinomio:
    def __init__(self,coefs,N):
        self.coefs=coefs
        self.N=N
    
    def imprimir(self):
        np=self.N
        for K in range(self.N+1):
            if self.coefs[K]!=1 and np!=0:
                print(end=""f"{self.coefs[K]}x^{np}+")
            elif self.coefs[K]==1:
                print(end=""f"x^{np}+")
            else:
                print(end=""f"{self.coefs[K]}")
            np-=1
        
def factorial(n):
    fact=1
    if n==0:
        return fact
    else:
        for i in range(1,n+1):
            fact*=i
    return fact

def potenciabin(A,N):
    coefs=[]
    for K in range(N+1):
        nk=factorial(N)/(factorial(K)*factorial(N-K))
        aK=A**K
        coefs.append(int(nk*aK))
    pol=Polinomio(coefs,N)
    pol.imprimir()
    
    
potenciabin(4,3)
        
