#Invertir una cadena de caracteres.

def invertir(cad):
    if len(cad)==1:
        return cad[0]
    else:
        return cad[len(cad)-1:len(cad)]+invertir(cad[:len(cad)-1])
    
print(invertir("cafe"))