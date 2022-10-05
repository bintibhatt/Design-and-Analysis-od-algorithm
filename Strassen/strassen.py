import numpy as np

def split(X):
    row,col=X.shape
    row2,col2=row//2,col//2
    a=X[:row2,:col2]
    b=X[:row2,col2:]
    c=X[row2:,:col2]
    d=X[row2:,col2:]
    return a,b,c,d

def strassen(X,Y):
    #base case
    if(len(X)==1):
        return X*Y
    a,b,c,d = split(X)
    e,f,g,h = split(Y)

    p1 = strassen(a,f-h)
    p2 = strassen(a+b,h)
    p3 = strassen(c+d,e)
    p4 = strassen(d, g-e)
    p5 = strassen(a+d,e+h)
    p6 = strassen(b-d,g+h)
    p7 = strassen(a-c,e+f)

    c11=p5+p4-p2+p6
    c12=p1+p2
    c21=p3+p4
    c22=p1+p5-p3-p7

    C=np.hstack((c11,c12)),np.hstack((c21,c22))
    return C
