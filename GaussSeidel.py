import numpy as np
import math

def GS(a,b):
    a=np.array(a)
    b=np.array(b)
    n=a.shape[0]
    x0=x0mat(n)
    d=np.diag(np.diag(a))
    lu=a-d
    dinv=np.linalg.inv(d)
    u=np.triu(a)-d
    l=np.tril(a)-d
    itnum=0
    xp=x0
    while itnum>=0:
        z1=np.linalg.inv(d+l)
        z2=b-(np.dot(u,xp))
        xn=np.dot(z1,z2)
        e=np.linalg.norm(xn-xp,2)
        if e<=0.0001:
            break
        itnum+=1
        xp=xn
    #print('number of iterations=',itnum)
    return xn
