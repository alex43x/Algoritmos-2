#Se pide construir un algoritmo que reciba esta matriz, que ha sido llenada por un jugador, y verifique si su contenido es válido de acuerdo a las reglas del juego, vale decir, si están presentes todos los barcos requeridos y si están colocados correctamente. Como resultado, el algoritmo deberá imprimir un mensaje adecuado en caso de que el contenido de la matriz esté de acuerdo con las reglas del juego o un mensaje de error si el contenido es incorrecto.

from random import randint
from ej1 import *
TAB=[["M", "M", "M", "B", "M", "B", "B", "B", "B", "B"],
     ["M", "M", "M", "B", "M", "M", "M", "M", "M", "M"],
     ["M", "M", "M", "B", "B", "M", "B", "B", "B", "M"],
     ["M", "M", "M", "M", "M", "M", "M", "M", "M", "M"],
     ["M", "M", "M", "B", "M", "M", "M", "M", "M", "M"],
     ["B", "M", "M", "B", "M", "B", "B", "B", "B", "M"],
     ["B", "M", "M", "B", "M", "M", "M", "M", "M", "M"],
     ["B", "M", "M", "M", "M", "M", "M", "M", "M", "M"],
     ["B", "M", "M", "B", "B", "B", "B", "M", "M", "M"],
     ["B", "M", "M", "M", "M", "M", "M", "M", "M", "M"]]

def in_bounds(i,j):
    return 0 <= i < 10 and 0 <= j < 10

def check_barco(A,i,j):
    """
    Revisa el barco que empieza en (i,j).
    Retorna (ok, mensaje).
    """
    # Detectar orientación
    orientacion = "S"   # barco de una sola celda
    if in_bounds(i+1,j) and A[i+1][j]=="B":
        orientacion = "V"
    elif in_bounds(i,j+1) and A[i][j+1]=="B":
        orientacion = "H"

    # Guardar coordenadas en listas separadas
    coords_x = []
    coords_y = []
    coords_x.append(i)
    coords_y.append(j)

    if orientacion=="V":
        k=i+1
        while k<10 and A[k][j]=="B":
            coords_x.append(k)
            coords_y.append(j)
            k+=1
    elif orientacion=="H":
        k=j+1
        while k<10 and A[i][k]=="B":
            coords_x.append(i)
            coords_y.append(k)
            k+=1

    largo = len(coords_x)

    # Revisar que no toque otros barcos (8 vecinos)
    for idx in range(largo):
        x = coords_x[idx]
        y = coords_y[idx]
        for dx in [-1,0,1]:
            for dy in [-1,0,1]:
                if dx==0 and dy==0:
                    continue
                nx = x+dx
                ny = y+dy
                if in_bounds(nx,ny) and A[nx][ny]=="B":
                    # revisar si pertenece al mismo barco
                    mismo = False
                    for k in range(largo):
                        if coords_x[k]==nx and coords_y[k]==ny:
                            mismo = True
                            break
                    if not mismo:
                        return False, "Error: barco en ("+str(x)+","+str(y)+") toca otro en ("+str(nx)+","+str(ny)+")"

    return True, "Barco válido de largo "+str(largo)

# --- MAIN ---
ok = True
for i in range(10):
    for j in range(10):
        if TAB[i][j]=="B":
            # inicio de barco si no hay B arriba ni a la izquierda
            if (i==0 or TAB[i-1][j]!="B") and (j==0 or TAB[i][j-1]!="B"):
                valido, msg = check_barco(TAB,i,j)
                print(msg)
                if not valido:
                    ok=False

if ok:
    print("Tablero válido")
else:
    print("Tablero inválido")
