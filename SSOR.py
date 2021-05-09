import numpy as np
import math
from numpy.linalg import multi_dot

def SSOR(a,b,w=1.2):
    a=np.array(a)
    b=np.array(b)
    i=a.shape[0]
    x0=x0mat(i)
    d=np.diag(np.diag(a))
    lu=a-d
    dinv=np.linalg.inv(d)
    u=np.triu(a)-d
    l=np.tril(a)-d
    itnum=0
    xp=x0
    i=np.identity(n[0])
    while itnum>=0:
        z1=np.linalg.inv(d+w*u)
        z2=np.linalg.inv(d+w*l)
        z3=(1-w)*d-w*l
        z4=(1-w)*d-w*u
        xn=multi_dot([z1,z3,z2,z4,xp])+multi_dot([w*z1,(np.dot(z3,z2)+i),b])
        e=np.linalg.norm(xn-xp,2)
        if e<=0.0001:
            #print('number of iterations:',itnum)
            break
        itnum+=1
        xp=xn
    return xn       
