#Preparar un programa que utilice el módulo “math” para imprimir la siguiente tabla de valores de
# funciones trigonométricas. Los valores deben redondearse a 5 decimales:

from math import sin,cos,tan,radians

print("Grados   sen      cos       tan")
for i in range(5,26,5):
    print(f"{i}        {round(sin(radians(i)),5)}   {round(cos(radians(i)),5)}   {round(tan(radians(i)),5)}")