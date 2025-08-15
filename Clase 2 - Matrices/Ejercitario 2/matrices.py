def creamat(M, N):
    MATRIZ = []
    for I in range(M):
        MATRIZ.append([0] * N)
    return (MATRIZ)

def leemat(MATRIZ):
    M = len(MATRIZ)
    N = len(MATRIZ[0])
    for I in range(M):
        for J in range(N):
            MATRIZ[I][J] = float(input("Ingrese el elemento (%d,%d): " % (I, J)))

def imprimat(MATRIZ):
    FILAS = len(MATRIZ)
    for I in range(FILAS):
        print(MATRIZ[I])