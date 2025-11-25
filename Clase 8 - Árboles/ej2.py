#IMPLEMENTACIÓN DE UN ÁRBOL BINARIO DE BÚSQUEDA 
#CON CREACIÓN DE LISTAS DE ELEMENTOS VISITADOS: L_INORDEN, L_PREORDEN, L_POSORDEN

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

class ABB:
    def __init__(self):
        self.raiz = None

    def agregar(self, valor): # agregar valor al árbol
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self._agregar(valor, self.raiz)

    def _agregar(self, valor, nodo_actual):
        if valor < nodo_actual.valor:
            if nodo_actual.izquierda is None:
                nodo_actual.izquierda = Nodo(valor)
            else:
                self._agregar(valor, nodo_actual.izquierda)
        elif valor > nodo_actual.valor:
            if nodo_actual.derecha is None:
                nodo_actual.derecha = Nodo(valor)
            else:
                self._agregar(valor, nodo_actual.derecha)

    def eliminar(self, valor): # eliminar valor al árbol
        if self.raiz is not None:
            self.raiz = self._eliminar(valor, self.raiz)

    def _eliminar(self, valor, nodo_actual):
        if nodo_actual is None:
            return nodo_actual

        if valor < nodo_actual.valor:
            nodo_actual.izquierda = self._eliminar(valor, nodo_actual.izquierda)
        elif valor > nodo_actual.valor:
            nodo_actual.derecha = self._eliminar(valor, nodo_actual.derecha)
        else:
            if nodo_actual.izquierda is None:
                temp = nodo_actual.derecha
                nodo_actual = None
                return temp
            elif nodo_actual.derecha is None:
                temp = nodo_actual.izquierda
                nodo_actual = None
                return temp
            temp = self._encontrar_min(nodo_actual.derecha)
            nodo_actual.valor = temp.valor
            nodo_actual.derecha = self._eliminar(temp.valor, nodo_actual.derecha)
        return nodo_actual

    def _encontrar_min(self, nodo_actual):
        while nodo_actual.izquierda is not None:
            nodo_actual = nodo_actual.izquierda
        return nodo_actual

    def modificar(self, valor, nuevo_valor): # reemplazar valor por nuevo_valor
        self.eliminar(valor)
        self.agregar(nuevo_valor)

    def imprimir(self): # imprimir arbol ordenado
        if self.raiz is not None:
            self._imprimir(self.raiz)

    def _imprimir(self, nodo_actual):
        if nodo_actual is not None:
            self._imprimir(nodo_actual.izquierda)
            print(str(nodo_actual.valor))
            self._imprimir(nodo_actual.derecha)

    def inorden(self): # recorrido inorden creando lista L_INORDEN con los nodos visitados
        if self.raiz is not None:
            self._inorden(self.raiz)

    def _inorden(self, nodo_actual):
        if nodo_actual is not None:
            self._inorden(nodo_actual.izquierda)
            L_INORDEN.append(nodo_actual.valor)
            self._inorden(nodo_actual.derecha)

    def preorden(self): # recorrido preorden creando lista L_PREORDEN con los nodos visitados
        if self.raiz is not None:
            self._preorden(self.raiz)

    def _preorden(self, nodo_actual):
        if nodo_actual is not None:
            L_PREORDEN.append(nodo_actual.valor)
            self._preorden(nodo_actual.izquierda)
            self._preorden(nodo_actual.derecha)

    def postorden(self): # recorrido postorden creando lista L_POSORDEN con los nodos visitados
        if self.raiz is not None:
            self._postorden(self.raiz)

    def _postorden(self, nodo_actual):
        if nodo_actual is not None:
            self._postorden(nodo_actual.izquierda)
            self._postorden(nodo_actual.derecha)
            L_POSORDEN.append(nodo_actual.valor)
            
def bst_max(lista):#la lista es el bst en inorden
    if not lista:
        return None
    nodo=Nodo(max(lista))
    mid=(len(lista))//2
    lista.remove(max(lista))
    izq=lista[:mid]
    der=lista[mid:]
    print(izq,der)
    nodo.izquierda=(bst_max(izq))
    nodo.derecha=(bst_max(der))
    return nodo
        
        
        

#PRUEBA DE FUNCIONAMIENTO

ARB=ABB()
LISTA = [30,80,10,40,60,90,20,50,70,45]
for VALOR in LISTA:
  ARB.agregar(VALOR)

L_INORDEN = []
L_PREORDEN = []
L_POSORDEN = []

print("\nLista original")
print (LISTA)

print("\nLista inorden")
ARB.inorden()
print (L_INORDEN)

print("\nLista preorden")
ARB.preorden()
print (L_PREORDEN)



BSTMAX=ABB()
BSTMAX.raiz=(bst_max(L_INORDEN))
print("\nLista postorden")
BSTMAX.postorden()
print (L_POSORDEN)
BSTMAX.imprimir()
  
