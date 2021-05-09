import numpy as np
import math

def SOR(a,b,w=1.2):
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
        z1=np.linalg.inv(d+w*l)
        z2=(w-1)*d+w*u
        xn=np.dot((np.dot(z1,z2)*-1),xp)+np.dot(w*z1,b)
        e=np.linalg.norm(xn-xp,2)
        if e<=0.0001:
            break
        itnum+=1
        xp=xn
    #print('number of iterations=',itnum)
    return xn
