#Obtener todas las palabras distintas que pueden formarse con cinco letras diferentes. No es necesario que las palabras tengan sentido.

def palabras(s):
    if len(s)==1:
        return s
    comb=[]
    for i in range(len(s)):
        resto=s[:i]+s[i+1:]
        for p in palabras(resto):
            comb.append(s[i]+p)
            
    return comb

n=palabras("abcde")
print(n, len(n))

