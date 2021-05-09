import numpy as np
import math
from numpy import linalg as la
import QRDecomposition-householder.py

def uppertriangular(a):
    n=a.shape[0]
    cnt=0
    epsilon=5*(10**-3)
    for i in range(n):
        for j in range(i):
            if a[i][j]>epsilon:
                cnt+=1
    if cnt==0:
        return True
    else:
        return False

def eignvalue_qr(a):
    a=np.array(a)
    eigns=[]
    n=a.shape[0]
    while uppertriangular(a)==False:
        q,r=qr_hh(a)
        a=np.dot(r,q)
    for i in range(n):
        eigns.append(a[i][i])
    return eigns
