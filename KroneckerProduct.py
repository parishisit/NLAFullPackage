import math
from numpy import linalg

def kronecker(a,b):
    m,n=a.shape[0],a.shape[1]
    p,q=b.shape[0],b.shape[1]
    c=[] 
    for i in range(m):
        for j in range(p):
            for k in range(n):
                for l in range(q):
                    c.append(a[i][k]*b[j][l])
    return np.reshape(c,(m*p,n*q))
