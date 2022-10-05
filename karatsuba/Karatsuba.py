#karatsuba approach for lonf integer multiplication
#using divide and conquer algorithmic paradigm

#perform X*Y
def karatsuba(X,Y):
    #base case : Atomic Multiplication
    if(X<10 or Y<10):
        return X*Y
    
    m = max(len(str(X)), len(str(Y)))  #unequal length

    if m%2!=0:
        m-=1
    a,b= divmod(X,10**(int(m/2)))
    c,d= divmod(Y,10**(int(m/2)))

    ac=karatsuba(a,c)
    bd=karatsuba(b,d)
    ab_cd=karatsuba((a+b),(c+d))-ac-bd

    return (ac*(10**m))+((ab_cd)*(10**int(m/2))) +bd

X = int(input("Enter number1: "))
Y = int(input("Enter NUmber2: "))
mul = karatsuba(X,Y)
print(mul)

def split(X):
    row,col=X.shape
    row2,col2=row//2,col//2
    a=X[:row2,:col2]
    b=X[:row2,col2:]
    c=X[row2:,:col2]
    d=X[row2:,col2:]
    return a,b,c,d

import numpy as np

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
