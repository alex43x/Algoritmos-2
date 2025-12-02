"""Geometria analitica TAA(2015)"""
from math import sqrt
class Recta:
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
    
class Punto:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        
def inters(r1,r2):
    x=((r1.b*r2.c)-(r1.c*r2.b))/((r1.a*r2.b)-(r1.b*r2.a))
    y=(((r2.a*r1.c)-(r2.c*r1.a))/((r1.a*r2.b)-(r1.b*r2.a)))
    Pi=Punto(x,y)
    print(Pi.x,Pi.y)
    return Pi

def dist(p1,p2):
    d=sqrt(pow(p1.x-p2.x,2)+pow(p1.y-p2.y,2))
    print(d)
    return d

def distrp(punto,recta):
    d=(abs(recta.a*punto.x+recta.b*punto.y+recta.c))/(sqrt(pow(recta.a,2)+pow(recta.b,2)))
    print(d)
    return d

r1=Recta(1,1,-3)
r2=Recta(1,2,-6)
r3=Recta(1,-2,-6)

inters(r1,r2)

p1=Punto(0,0)
p2=Punto(3,4)

dist(p1,p2)

distrp(p1,r1)

pi1=inters(r1,r2)
pi2=inters(r1,r3)
pi3=inters(r2,r3)
base=dist(pi1,pi2)
altura=distrp(pi3,r1)
print(base*altura/2)