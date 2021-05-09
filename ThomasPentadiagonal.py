import numpy asnp
import math

def thomas_5(a,b):
    a=np.array(a)
    b=np.array(b)
    n=a.shape[0]
    x=[]
    for i in range(n-1):
        pivot=a[i][i]
        for j in range(i+1,i+3):
            if j<n:
                m=-1*a[j][i]/pivot
                for k in range(i,i+3):
                    if k<n:
                        a[j][k]+=m*a[i][k]
                b[j]+=m*b[i]
    
            
    for p in range(n-1,-1,-1):
        x.insert(0,b[p]/a[p][p])
        if p>0:
            b[p-1]=b[p-1]-x[0]*a[p-1][p]
    return x  
