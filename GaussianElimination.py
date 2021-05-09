import numpy as np
import math

def gauss_elimination(a,b):
    a=np.array(a)
    b=np.array(b)
    n=a.shape[0]
    x=[]
    for i in range(n-1):
        pivot=a[i][i]
        for j in range(i+1,n):
            m=-1*a[j][i]/pivot
            for k in range(0,n):
                a[j][k]+=m*a[i][k]
            b[j]+=m*b[i]
            
    for p in range(n-1,-1,-1):
        x.append(b[p]/a[p][p])
        for q in range(p-1,-1,-1):
            b[q]=b[q]-x[n-p-1]*a[q][p]
    return x
