#Escribir un módulo “fechas.py” para implementar un tipo de datos adecuado para representar fechas en formato DD, MM, AA y realizar las siguientes operaciones con ellas:

from datetime import date

def bisiesto (aa):
    if (aa%400==0)or (aa%4==0 and aa%100!=0):
        return 1
    else:
        return 0
    
def fecha_a_dias(f):
    dias=0
    for i in range(1,f.aa):
        if bisiesto(i)==1:
            dias+=366
        else:
            dias+=365
    
    if bisiesto(f.aa)==1:
        months=[31,29,31,30,31,30,31,31,30,31,30,31]
    else:
        months=[31,28,31,30,31,30,31,31,30,31,30,31]
    
    for i in range(f.mm-1):
        dias+=months[i]
        
    dias+=f.dd               
    

def fecha(dias):
    aa=1950
    resto=dias
    while resto>364: 
        if bisiesto(aa)==0:
            resto-=365
        else:
            resto-=366
        aa+=1
    
    if bisiesto(aa)==1:
        months=[31,29,31,30,31,30,31,31,30,31,30,31]
    else:
        months=[31,28,31,30,31,30,31,31,30,31,30,31]
    mm=0
    
    while resto>=months[mm]:
        resto-=months[mm]
        mm+=1
    
    fecha=Fecha(resto+1,mm+1,aa)
    print(resto+1, aa,mm+1)
    return fecha

def dias(f1,f2):
    d1=fecha_a_dias(f1)
    d2=fecha_a_dias(f2)
    return abs(d2-d1)

def pasado(f,d):
    resto=d
    
    if bisiesto(f.aa)==1:
        months=[31,29,31,30,31,30,31,31,30,31,30,31]
    else:
        months=[31,28,31,30,31,30,31,31,30,31,30,31]
    resto+=months[f.mm-1]-f.dd+1
    for i in range(f.mm,12):
        resto+=months[i]
    print(resto)
    aa=f.aa
    while resto>364: 
        if bisiesto(aa)==0:
            resto-=365
        else:
            resto-=366
        aa-=1
    
    if bisiesto(aa)==1:
        months=[31,29,31,30,31,30,31,31,30,31,30,31]
    else:
        months=[31,28,31,30,31,30,31,31,30,31,30,31]
    mm=11
    
    while resto>=months[mm]:
        resto-=months[mm]
        mm-=1
    
    fecha=Fecha(months[mm]-resto+1,mm+1,aa)
    print("Pasado:",months[mm]-resto+1, aa,mm+1)
    return fecha

def futuro(f,d):
    resto=d
    
    if bisiesto(f.aa)==1:
        months=[31,29,31,30,31,30,31,31,30,31,30,31]
    else:
        months=[31,28,31,30,31,30,31,31,30,31,30,31]
    for i in range(f.mm-1):
        resto+=months[i]
        
    resto+=f.dd-1
    
    aa=f.aa
    while resto>364: 
        if bisiesto(aa)==0:
            resto-=365
        else:
            resto-=366
        aa+=1
    
    if bisiesto(aa)==1:
        months=[31,29,31,30,31,30,31,31,30,31,30,31]
    else:
        months=[31,28,31,30,31,30,31,31,30,31,30,31]
    mm=0
    
    while resto>=months[mm]:
        resto-=months[mm]
        mm+=1
    
    fecha=Fecha(resto+1,mm+1,aa)
    print("Futuro:",resto+1, aa,mm+1)
    return fecha      

class Fecha:
    def __init__(self,dd,mm,aa):
        self.dd=dd
        self.mm=mm
        self.aa=aa
    
    def dias(self):
        days=0
        for i in range(1950,self.aa):
            bs=bisiesto(i)
            if bs==0:
                days+=365
            else:
                days+=366
        if bisiesto(self.aa)==1:
            months=[31,29,31,30,31,30,31,31,30,31,30,31]
        else:
            months=[31,28,31,30,31,30,31,31,30,31,30,31]
        for i in range(self.mm-1):
            days+=months[i]
        days+=self.dd-1
        print(days)
        return days
    
def diasem(f):
    f = date(f.aa, f.mm, f.dd)
    dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    return dias[f.weekday()]
    
def validafecha(f):
    if bisiesto(f.aa)==1:
        months=[31,29,31,30,31,30,31,31,30,31,30,31]
    else:
        months=[31,28,31,30,31,30,31,31,30,31,30,31]  
        
    if f.mm<1 or f.mm>12:
        return False
    if f.dd<months[f.mm-1]:
        return False
    return True

def bs(f):
    if bisiesto(f.aa)==1:
        return True
    else:
        return False
    
def textofecha(f):
    months=["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]
    ft=f"{f.dd} de {months[f.mm-1]} de {f.aa}"
    return ft
            
            
f=Fecha(24,8,2025)
        
f.dias()

fecha(27628)

futuro(f,365)
pasado(f,365)

print(diasem(f))
print(textofecha(f))

        
                