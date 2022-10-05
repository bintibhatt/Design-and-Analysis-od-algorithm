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