"""
#PROBLEMA
La matriz MAR, de M filas y N columnas, representa el mapa de una zona marítima en la cual se observa un
conjunto de islas. Las celdas con valor cero representan agua y las celdas con valor uno representan tierra.
Ninguna de estas islas toca los bordes de la matriz (el gráfico muestra cómo podría ser la matriz MAR).
Un barco de guardacostas está anclado en la posición conocida MAR(F,C) y debe partir de allí para realizar
una misión de vigilancia recorriendo el perímetro completo de cada una de las islas siguiendo un sentido
antihorario.
En su viaje, el capitán sigue la siguiente estrategia para economizar combustible:
a) Localiza la isla más cercana a su posición actual;
b) Se dirige a dicha isla siguiendo el camino más corto posible (pasando siempre de una celda a otra
adyacente sin salir nunca de la matriz);
c) Recorre la playa en sentido antihorario; y,
d) Vuelve al paso (a).
Escribir un algoritmo que solicite los datos del problema y calcule e imprima la posición de las celdas por las
que pasará el barco hasta completar su trabajo y volver a su posición inicial."""

MAR = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 0, 1, 1, 0, 0],
    [0, 1, 1, 1, 0, 0, 1, 1, 1, 0],
    [0, 1, 1, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 1, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

class Cola():
    def __init__(self):
        self.items=[]
        
    def vacia(self):
        return len(self.items)==0
    
    def agregar(self,item):
        self.items.append(item)
        
    def sacar(self):
        self.items.pop(0)
        
    def tamano(self):
        return len(self.items)
        

F = 6  # Fila inicial (centro)
C = 8  # Columna inicial (centro)

# Número de islas esperadas: 3
def valid(MAR,x,y,visitados):
    if x<0 or x>7 or y<0 or y>9 or [x,y] in visitados:
        return False
    return True

def localizar(MAR,x,y,dist):
    visitados=[]
    opciones=Cola()
    opciones.agregar([[x,y],dist])
    while opciones.vacia()==False:
        dist=opciones.items[0][1]+1
        x=opciones.items[0][0][0]
        y=opciones.items[0][0][1]
        visitados.append([x,y])
        if valid(MAR,x+1,y,visitados)==True:
            opciones.agregar([[x+1,y],dist])
        if valid(MAR,x-1,y,visitados)==True:
            opciones.agregar([[x-1,y],dist])
        if valid(MAR,x,y+1,visitados)==True:
            opciones.agregar([[x,y+1],dist])
        if valid(MAR,x,y-1,visitados)==True:
            opciones.agregar([[x,y-1],dist])
        print(opciones.items)
        print()
        if MAR[x][y]==1:
            return opciones.items[0]
        opciones.sacar()
        

localizar(MAR,F,C,0)
print(localizar(MAR,F,C,0))
    