#Dada una cadena que contiene paréntesis (, ), llaves {, } y corchetes [, escribe una función que determine si la cadena está bien formada. Es decir, si los paréntesis, llaves y corchetes están correctamente anidados y cerrados en el orden correcto.

class Pila():
    def __init__(self):
        self.items=[]
        
    def vacia(self):
        return len(self.items)==0

    def apilar(self,elemento):
        self.items.append(elemento)
    
    def desapilar(self):
        self.items.pop()
        
    def tope(self):
        return self.items[-1]
    
    def tamano(self):
        return len(self.items)
    
cad="[{{({})}}]"

def check_cad(cad):
    valid=True
    sec=Pila()
    i=0
    while i<len(cad) and valid==True:
        if cad[i]=="[" or cad[i]=="{" or cad[i]=="(":
            sec.apilar(cad[i])
        elif cad[i]=="]":
            if sec.tope()=="[":
                sec.desapilar()
            else:
                valid=False
        elif cad[i]=="}":
            if sec.tope()=="{":
                sec.desapilar()
            else:
                valid=False
        elif sec.tope()=="(":
            sec.desapilar()
        else:
            valid=False
        i+=1
    
    return valid
                
            
print(check_cad(cad))