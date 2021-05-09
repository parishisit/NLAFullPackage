import numpy as np
import math
from numpy import linalg
import KroneckerProduct.py

def solve(A,B,C):
    A,B,C=np.array(A),np.array(B),np.array(C) 
    n=A.shape[0]
    m=B.shape[0]
    a_prime=kronecker(A,np.identity(m))
    b_prime=kronecker(np.identity(n),np.transpose(B))
    a=a_prime+b_prime
    b=np.reshape(C,(m*n,1))
    return a,b
