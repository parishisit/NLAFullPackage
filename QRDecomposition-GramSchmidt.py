import numpy as np
import math
from numpy import linalg as la

def qr_gs(a):
    a=np.array(a)
    m=a.shape[0]
    n=a.shape[1]
    r=np.zeros((n,n))
    qt=np.zeros((n,m))
    pt=np.zeros((n,m))
    at=np.transpose(a)
    r[0][0]=math.sqrt(np.dot(at[0],at[0]))
    qt[0]=at[0]/r[0][0]
    for j in range(1,n):
        z=0
        for i in range(j-1):
            r[i][j]=np.dot(qt[i],at[j])
            z+=r[i][j]*qt[i]
        pt[j]=at[j]-z
        r[j][j]=math.sqrt(np.dot(pt[j],pt[j]))
        qt[j]=pt[j]/r[j][j]
        
    q=np.transpose(qt)
    return q,r
