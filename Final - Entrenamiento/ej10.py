"""Corren tiempos festivos y los Reyes Magos se preparan para su tradicional visita a los niños del
mundo.
Como cada año, Melchor y Gaspar elaboran la lista ACT de actividades que deben realizar para
cumplir con su cometido."""

ACT=[[1,"a",4],
     [2,"b",5],
     [3,"c",3],
     [4,"d",5],
     [5,"e",2],
     [6,"f",4],
     [7,"g",2],
     [8,"h",1],
     [9,"i",1]]

REL=[["a","b"],
     ["a","c"],
     ["b","d"],
     ["b","e"],
     ["c","f"],
     ["d","g"],
     ["e","h"],
     ["f","h"],
     ["g","i"],
     ["h","i"],
     ]

def dias_actividad(ACT,av):
    for i in range(len(ACT)):
        if ACT[i][1]==av:
            return ACT[i][2]
            

def calcular_dias(ACT,REL,av):
    days=dias_actividad(ACT,av)
    dep=0
    for i in range(len(REL)):
        if REL[i][1]==av:
            n=calcular_dias(ACT,REL,REL[i][0])
            if dep<n:
                dep=n
    print(av,days,dep)
    return days+dep

print(calcular_dias(ACT,REL,"i"))
    
    