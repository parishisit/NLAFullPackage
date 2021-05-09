import numpy asnp
import math

def thomas_3(a,b):
    a=np.array(a)
    b=np.array(b)
    n=a.shape[0]
    x=[]
    for i in range(n-1):
        pivot=a[i][i]
        m=-1*a[i+1][i]/pivot
        a[i+1][i]=0
        a[i+1][i+1]+=m*a[i][i+1]
        b[i+1]+=m*b[i]
    
            
    for p in range(n-1,-1,-1):
        x.insert(0,b[p]/a[p][p])
        if p>0:
            b[p-1]=b[p-1]-x[0]*a[p-1][p]
    return x  
