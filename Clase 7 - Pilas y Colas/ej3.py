#Dado un laberinto, escribe un programa que encuentre una ruta desde la entrada hasta la salida. El laberinto es representado como una matriz de caracteres donde . representa un espacio vacío y # representa un obstáculo. El programa debe utilizar una pila para llevar un registro de los movimientos realizados.

class Pila():
    def __init__(self):
        self.items=[]
        
    def vacia(self):
        return len(self.items)==0

    def apilar(self,elemento):
        self.items.append(elemento)
    
    def desapilar(self):
        return self.items.pop()
        
    def tope(self):
        return self.items[-1]
    
    def tamano(self):
        return len(self.items)

Lab=[["#","#","#","#","#"],
     [".",".","#",".","#"],
     ["#",".",".",".","#"],
     ["#","#",".","#","#"],
     ["#","#",".",".","."],
     ["#","#","#","#","#"]]


#1-izquierda, 2-arriba, 3-derecha, 4-abajo
def laberinto(L,x,y,movs,visited):
    print(movs.items)
    visited.append([x,y])
    if [x, y] == [4, 4]:
        return True
    
    visited.append([x, y])
    
    if x+1 < len(L) and L[x+1][y]!="#" and [x+1, y] not in visited:
        movs.apilar(4)
        if laberinto(L,x+1,y,movs,visited):
            return True
        movs.desapilar()
    
    if x-1 >= 0 and L[x-1][y]!="#" and [x-1, y] not in visited:
        movs.apilar(2)
        if laberinto(L,x-1,y,movs,visited):
            return True
        movs.desapilar()
    
    if y+1 < len(L[0]) and L[x][y+1]!="#" and [x, y+1] not in visited:
        movs.apilar(3)
        if laberinto(L,x,y+1,movs,visited):
            return True
        movs.desapilar()
    
    if y-1>=0 and L[x][y-1]!="#" and [x, y-1] not in visited:
        movs.apilar(1)
        if laberinto(L,x,y-1,movs,visited):
            return True
        movs.desapilar()
    
    return False
    
        
visited=[]     
movs=Pila()
laberinto(Lab,1,0,movs,visited)   