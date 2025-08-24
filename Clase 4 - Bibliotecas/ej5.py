#Preparar un programa para calcular el tiempo trabajado por un empleado en formato HH:MM:SS, dado el horario de entrada y de salida, utilizando el módulo “time”.

from time import strptime

ent_str=str(input("Ingrese horario de entrada en formato hh:mm:ss"))
sal_str=str(input("Ingrese horario de salida en formato hh:mm:ss"))

ent=strptime(ent_str, "%H:%M:%S")
sal=strptime(sal_str, "%H:%M:%S")

ens=sal.tm_hour*3600+sal.tm_min*60+sal.tm_sec-(ent.tm_hour*3600+ent.tm_min*60+ent.tm_sec)

horas,resto=ens//3600,ens%3600

minutos,resto=resto//60,resto%60

print(f"Pasaron {horas}:{minutos}:{resto}")


