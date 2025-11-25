#Dada una cadena de caracteres, escribe un programa que encuentre el primer carácter no repetido en la cadena. El programa debe utilizar dos colas, una para almacenar los caracteres encontrados hasta el momento y otra para almacenar los caracteres pendientes de procesar.

class Cola():
    def __init__(self):
        self.items=[]
    
    def vacia(self):
        return len(self.items)==0
    
    def agregar(self,elemento):
        self.items.append(elemento)
    
    def sacar(self):
        return self.items.pop(0)
    
    def tamano(self):
        return len(self.items)
    
def repetido(cad):
    pendiente=Cola()
    procesado=Cola()
    
    for i in cad:
        pendiente.agregar(i)
    valid=True
    while pendiente.vacia()==False and valid==True:
        if pendiente.items[0] in procesado.items:
            valid=False
        else:
            procesado.agregar(pendiente.items[0])
            pendiente.sacar()
    
    return valid

c1="aabc"
c2="abcd"

print(repetido(c1))
print(repetido(c2))