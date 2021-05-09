import numpy as np
import math
from numpy import linalg as la
import QRDecomposition-householder.py

def solve(a,b):
    y=[]
    x=[]
    a=np.array(a)
    n=a.shape[0]
    b=np.array(b)
    q,r=qr_hh(a)
    #qrx=b , rx=y
    #first eq : y=qt.b
    qt=np.transpose(q)
    y=np.dot(qt,b)
    #second eq rx=y
    for p in range(n-1,-1,-1):
        x.insert(0,y[p]/r[p][p])
        for s in range(p-1,-1,-1):
            y[s]=y[s]-x[0]*r[s][p]
    return x
