"""PROBLEMA PROPUESTO
Un supermercado posee P cajas, numeradas de 1 a P, encargadas de realizar la cobranza a los clientes.
Se requiere diseñar las estructuras de datos requeridas para representar los elementos del siguiente problema
y construir un algoritmo Python capaz de:
1) Generar una cola de N clientes. Cada cliente tiene asociado los siguientes datos:
a. Número de cliente: secuencial, de 1 a N.
b. Cantidad de artículos en su carrito: valor aleatorio, entre 5 y 30.
A las 10:00:00 horas todas las cajas están libres y los clientes de la cola generada empiezan a pasar
ordenadamente a las cajas. Cada cliente elige la caja que menos clientes tenga en este momento. Si
varias cajas tienen el mismo número de clientes, el cliente elige aquella que tenga el menor número de
caja. El tiempo de atención en la caja es de 10 segundos por cada artículo en el carrito.
2) Simular el funcionamiento del sistema de colas desde las 10:00:00 horas hasta que los N clientes
hayan sido atendidos.
3) Para cada cliente calcular e imprimir: en cuál caja y a qué hora exacta (horas, minutos y segundos)
termina de ser atendido."""

from datetime import *
from random import randint

def sumar_tiempo(segundos):
    hora=datetime(2025,1,1,10,0,0)
    nueva_hora=hora+timedelta(seconds=segundos)
    return nueva_hora.strftime("%H:%M:%S")

class Cliente:
    def __init__(self,id,arts):
        self.id=id
        self.arts=arts

N=15              
P=10              
cola=[]
for i in range(0,N):
    cli=Cliente(i+1,randint(5,30))
    cola.append(cli)
    print(cola[i].id,cola[i].arts)
cajas=[0]*P
segundos=0



print(f"Cliente\tCaja\tHora salida")
sw=True
while len(cola)>0 or sw==True:
    c=0
    if segundos>0:
        for i in range(P):
            if cajas[i] !=0:
                if ((cajas[i][0].arts)*10)+cajas[i][1]-segundos==0:
                    print(f"{cajas[i][0].id}\tN°{i+1}\t{sumar_tiempo(segundos)}")
                    cajas[i]=0
    #revisa si hay uno libre
    for i in range(P):
        if cajas[i]==0 and len(cola)>0:
            cajas[i]=[cola[0],segundos]
            cola.pop(0)
    for i in range(P):
        if cajas[i]==0:
            c+=1
    if c==10:
        sw=False
    segundos+=10


print(sumar_tiempo(90))