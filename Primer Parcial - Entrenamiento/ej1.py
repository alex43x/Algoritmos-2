#Tomando como referencia el módulo “matrices” desarrollado previamente, construir un nuevo módulo denominado “matricesalfa” adecuado para el manejo de matrices cuyos elementos sean cadenas de caracteres.

def creamat(M, N):
    MATRIZ = []
    for I in range(M):
        MATRIZ.append([""] * N)
    return (MATRIZ)

def leemat(MATRIZ):
    M = len(MATRIZ)
    N = len(MATRIZ[0])
    for I in range(M):
        for J in range(N):
            MATRIZ[I][J] = (input("Ingrese el elemento (%d,%d): " % (I, J)))

def imprimat(MATRIZ):
    FILAS = len(MATRIZ)
    for I in range(FILAS):
        print(MATRIZ[I])