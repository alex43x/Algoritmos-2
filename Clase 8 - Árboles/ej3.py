#Se necesita escribir un algoritmo en Python que reciba las dos listas preparadas y calculé ¿cuántos días se requieren desde el inicio de la primera actividad hasta completar todas las actividades previstas?

ACT=[["a","...",2],
     ["b","...",3],
     ["c","...",4],
     ["d","...",2],
     ["e","...",5],
     ["f","...",1]]

REL=[["e","f"],
     ["b","f"],
     ["c","e"],
     ["c","d"],
     ["a","c"],
     ["a","b"]]

def time_required(act):
    t=0
    for i in range(len(ACT)):
        if ACT[i][0]==act:
            t+=ACT[i][2]     
    may=0
    for i in range(len(REL)):
        if REL[i][1]==act:
            nt=time_required(REL[i][0])
            if nt>may:
                may=nt
            
    return t+may

def calc_time(ACT,REL):
    may=0
    for i in range(len(ACT)):
        t=time_required(ACT[i][0])
        if t>may:
            may=t
            
    return may

print(time_required("a"))
print(time_required("b"))
print(time_required("c"))
print(time_required("d"))
print(time_required("e"))
print(time_required("f"))
print(calc_time(ACT,REL))