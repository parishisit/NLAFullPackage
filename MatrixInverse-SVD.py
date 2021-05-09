import numpy as np
import math
from numpy import linalg as la
import SVD.py

def a_prep(a):
    m=a.shape[0]
    n=a.shape[1]
    u,sigma,vt=svd(a)
    sigma_prep=np.zeros((n,m))
    s=np.diag(sigma)
    s_inv=[1/x for x in s]
    for i in range(m):
        sigma_prep[i][i]=s_inv[i]
    a_prep=la.multi_dot([np.transpose(vt),sigma_prep,np.transpose(u)])
    return a_prep
