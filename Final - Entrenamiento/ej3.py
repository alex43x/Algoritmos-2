"""Se tiene como datos un valor entero S y un árbol binario BIN en el que cada nodo contiene:
• nombre: una cadena única que identifica al nodo.
• valor: un número entero.
Escribir un programa Python para leer los datos indicados y luego encontrar un recorrido desde la
raíz del árbol hacia sus descendientes, de modo que la suma de los valores de los nodos visitados
sea exactamente igual al valor S. Al concluir, el programa deberá indicar los nombres de los nodos
que deben visitarse en el orden correspondiente.
El procedimiento de lectura del árbol debe ser: a) leer la cantidad de nodos; b) leer nombre y valor de
la raíz; c) para cada nodo, leer nombre, valor del nodo y nombre del padre del nodo. Asumir que todos
los datos son correctos, no se requiere validación alguna.
En el recorrido solo se puede avanzar desde un nodo hacia sus hijos, es decir, la suma debe
obtenerse recorriendo el camino desde la raíz hasta descendientes de nivel inferior.
El recorrido puede detenerse en cualquier nodo, no es necesario llegar a las hojas.
Si no se encuentra ningún camino que cumpla la condición, devolver el mensaje de error: “no existe
solución”.
"""

class Nodo:
    def __init__(self,nombre,valor,padre,izq,der):
        self.nombre=nombre
        self.valor=valor
        self.padre=padre
        self.izq=izq
        self.der=der

class Arbol:
    def __init__(self,raiz):
        self.raiz=raiz
    
    def agregar(self,nombre,valor,padre,nodo_actual):
        if nodo_actual is None:
            nodo_actual=self.raiz
        if nodo_actual is None: 
            return False
        if nodo_actual.nombre==padre:
            if nodo_actual.izq is None:
                nodo_actual.izq=Nodo(nombre,valor,nodo_actual.nombre,None,None)
                return True
            elif nodo_actual.der is None:
                nodo_actual.der=Nodo(nombre,valor,nodo_actual.nombre,None,None)
                return True
            else:
                return False
        if nodo_actual.izq is not None:
            if self.agregar(nombre,valor,padre,nodo_actual.izq):
                return True
        if nodo_actual.der is not None:
            if self.agregar(nombre,valor,padre,nodo_actual.der):
                return True
        return False
    
    def mostrar_arbol(self, nodo=None, nivel=0):
        if nodo is None:
            nodo = self.raiz
        
        if nodo is None:
            return
        
        print("  " * nivel + f"{nodo.nombre}({nodo.valor})")
        
        if nodo.izq:
            self.mostrar_arbol(nodo.izq, nivel + 1)
        if nodo.der:
            self.mostrar_arbol(nodo.der, nivel + 1)
    
    def sumar(self,valor,nodo_actual,camino,ac=0):
        if nodo_actual is None:
            nodo_actual=self.raiz
            camino=[]
        ac+=nodo_actual.valor
        if ac>valor:
            return None
        elif ac==valor:
            camino.append(nodo_actual.nombre)
            return camino
        else:
            copy_camino=camino.copy()
            copy_camino.append(nodo_actual.nombre)
            if nodo_actual.izq is not None:
                res=self.sumar(valor,nodo_actual.izq,copy_camino,ac)
                if res is not None:
                    return res
            if nodo_actual.der is not None:
                res=self.sumar(valor,nodo_actual.der,copy_camino,ac)
                if res is not None:
                    return res
            
        return None


raiz=Nodo("A",5,None,None,None)
arbolito=Arbol(raiz)
arbolito.agregar("B",3,"A",None)    
arbolito.agregar("C",8,"A",None)    
arbolito.agregar("D",2,"B",None)    
arbolito.agregar("E",4,"B",None)    
arbolito.agregar("F",1,"C",None)

arbolito.mostrar_arbol()

print(arbolito.sumar(12,None,None))
            
        
            
            
            
        