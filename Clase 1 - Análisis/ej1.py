#Calcular la cantidad de dias transcurridos hasta una fecha especifica desde el 01/01/1980

#Análisis
#Se debe tomar en cuenta la diferencia de dias entre cada mes, se recibirán los datos en formato dd/mm/aaaa pero por separado

#Solución
#Restar, empezando desde los días, luego meses, y por ultimos los años 

def bisiesto (aa):
    if (aa%400==0)or (aa%4==0 and aa%4!=0):
        bs=1
    else:
        bs=0

aa=int(input("Ingrese año"))
mm=int(input("Ingrese mes"))
dd=int(input("Ingrese día"))-1
bs=0
dif=0
while aa<1980 :
    print("El año debe ser superior a 1980")
    aa=int(input("Ingrese año"))

while mm<1 or mm>12:
    print("El mes debe ser un valor entre 1 y 12")
    mm=int(input("Ingrese mes"))

for i in range(1980,aa):
    if bisiesto(i)==0:
        dif+=365
    else:
        dif+=366

if mm==1:
    dif+=dd
elif mm==2:
    dif+=dd+31
elif mm==3:
    dif+=dd+59
elif mm==4:
    dif+=dd+90
elif mm==5:
    dif+=dd+120
elif mm==6:
    dif+=dd+151
elif mm==7:
    dif+=dd+181
elif mm==8:
    dif+=dd+212
elif mm==9:
    dif+=dd+243
elif mm==10:
    dif+=dd+273
elif mm==11:
    dif+=dd+304
else:
    dif+=dd+334

print("La cantidad de dias que trasncurrieron son", dif)

