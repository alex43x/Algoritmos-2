#12.Ordenar una lista utilizando el método Quick Sort.

L=[4,7,3,9,1]
def quick_sort(L):
    if len(L)<=1:
        return L
    else:
        p=L[0]
        men=[]
        may=[]
        for i in range(1,len(L)):
            if L[i]<p:
                men.append(L[i])
            else:
                may.append(L[i])
        return quick_sort(men)+[p]+quick_sort(may)
    
print(quick_sort(L))