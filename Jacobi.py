import numpy as np
import math

def jacobi(a,b):
    a=np.array(a)
    b=np.array(b)
    n=a.shape[0]
    x0=np.zeros((n,1))
    d=np.diag(np.diag(a))
    lu=a-d
    dinv=np.linalg.inv(d)
    u=np.triu(a)-d
    l=np.tril(a)-d
    itnum=0
    xp=x0
    while itnum>=0:
        z1=np.dot(l+u,xp)
        xn=np.dot(dinv,b-z1)
        e=np.linalg.norm(xn-xp,2)
        if e<=0.0001:
            break
        itnum+=1
        xp=xn
    #print('number of iterations=',itnum)
    return xn
