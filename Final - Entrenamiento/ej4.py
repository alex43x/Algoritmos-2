"""
Polinomios TAA(2016)
"""

class Polinomio:
    def __init__(self,coefs):
        self.coefs=coefs
    
def imprimir(self):
    for i in range(len(self.coefs)):
        if self.coefs[i]>=0 and i!=0:
            print(f"+{self.coefs[i]}x^{len(self.coefs)-i-1}",end="")
        else:
            print(f"{self.coefs[i]}x^{len(self.coefs)-i-1}",end="")
    print()
            

def multipol(a,b):
    new_coefs=[0]*(len(a.coefs)-1+len(b.coefs))
    print(new_coefs)
    for i in range(len(a.coefs)):
        for j in range(len(b.coefs)):
            new_coefs[i+j]+=a.coefs[i]*b.coefs[j]
    pol=Polinomio(new_coefs)
    return pol

def raices(raices):
    pols=[]
    for i in range(len(raices)):
        pol=Polinomio([1,-raices[i]])
        pols.append(pol)
    if len(raices)==1:
        pol=Polinomio([1,-raices[0]])
        return pol
    pol=multipol(pols[0],pols[1])
    pols.pop(0)
    pols.pop(0)
    if len(raices)==0:
        return pol
    else:
        while len(pols)>0:
            pol=multipol(pol,pols[0])
            pols.pop(0)
        return pol

    
    
    
pol1=Polinomio([3,-2,1])
pol2=Polinomio([4,2])
imprimir(pol1)
imprimir(pol2)

mult=multipol(pol1,pol2)
imprimir(mult)

r=raices([1,2,3])
imprimir(r)