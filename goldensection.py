from sympy import *
import numpy as np

w= float(input("Term coefficient with 4 power of x:"))
a= float(input("Term coefficient with 3 power of x:"))
b= float(input("Term coefficient with 2 power of x:"))
d= float(input("Term coefficient with 1 power of x:"))
c= float(input("constant term:"))

x = Symbol('x')
y = w*(x**4) + a*(x**3) + b*(x**2) + d*(x) + c

a=float(input("a :"))
b=float(input("b :"))
k=int(input("iteration number :"))

for i in range (0,k+1):
    x1= b - 0.618*(b-a)
    x2= a + 0.618*(b-a)
    print("x",i+(i+1),"=",x1,", x",i+(i+2),"=",x2)
    
    if y.subs('x',x1) < y.subs('x',x2):
        a= x1
        print("new range values:",a,",",b)
        print("new range:", (b-a))
        
    if y.subs('x',x1) > y.subs('x',x2):
        b= x2
        print("new range values:",a,",",b)
        print("new range:", (b-a))
        
    print("_________________________________________")    
    
    
    
    



