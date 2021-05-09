import numpy as np
import math
from numpy import linalg as la

def svd(a):
    m=a.shape[0]
    n=a.shape[1]
    at=np.transpose(a)
    mat=np.dot(at,a)
    u=np.zeros((m,m))
    v=np.zeros((n,n))
    _eignvals , _eignvects = la.eig(mat)
    eignvals=np.flip(_eignvals)
    eignvects=np.flip(_eignvects,axis=1)
    s=[math.sqrt(val) for val in eignvals]
    for i in range(n):
        v[:,i]=eignvects[:,i]/la.norm(eignvects[:,i],2)
    vt=np.transpose(v)
    sigma=np.zeros((m,n))
    for i in range(m):
        sigma[i][i]=s[i]
    for j in range(m):
        u[:,j]=(1/s[j])*(np.dot(a,v[:,j]))
    return u,sigma,vt
