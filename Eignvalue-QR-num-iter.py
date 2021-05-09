import numpy as np
import math
from numpy import linalg as la
import QRDecomposition-householder.py

def eignvalue_qr_m(a,num_iter):
    eigns=[]
    n=a.shape[0]
    for j in range(num_iter):
        q,r=qr_hh(a)
        a=np.dot(r,q)
    for i in range(n):
        eigns.append(a[i][i])
    return eigns
