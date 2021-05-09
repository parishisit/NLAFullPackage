import numpy as np
import math

def pivoting(a,n,i):
    max_index=i
    for index in range(i+1,n):
        if abs(a[index][i])>abs(a[max_index][i]):
            max_index=index
    return max_index 


def LU_pivoting(a,b):
    m=[]
    x=[]
    y=[]
    a=np.array(a)
    b=np.array(b)
    n=a.shape[0]
    l=np.ones((n,n))
    for i in range(n):
        new_index=pivoting(a,n,i)
        a[i],a[new_index]=a[new_index],a[i]
        b[i],b[new_index]=b[new_index],b[i]
        pivot=a[i][i]
        for j in range(0,n):
            if j<i:
                l[j][i]=0
            elif j>i:
                m=-1*a[j][i]/pivot
                l[j][i]=-m
                for k in range(0,n):
                    a[j][k]+=m*a[i][k]
    u=a
    
    
    #first eq ly=b solving
    for p in range(0,n):
        y.append(b[p]/l[p][p])
        for q in range(p+1,n):
            b[q]=b[q]-y[p]*l[q][p]
    

    #second eq solving
    for r in range(n-1,-1,-1):
        x.insert(0,y[r]/u[r][r])
        for s in range(r-1,-1,-1):
            y[s]=y[s]-x[0]*u[s][r]
    
    return x 
