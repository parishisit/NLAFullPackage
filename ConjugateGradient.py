import numpy as np

def CG(a,b,x0=None):
    a=np.array(a)
    b=np.array(b)
    n=a.shape[0]
    x0=np.ones((n,1))
    p=b-a@x0
    r=b-a@x0
    x=x0
    for i in range(n):
        r_norm_1=r.T @ r
        alpha=(r.T @ r) / (p.T @ a @ p)
        x+=alpha * p
        r-=alpha * (a @ p)
        r_norm_2=r.T @ r
        beta= - r_norm_2/r_norm_1
        p=beta*p + r
    return x
