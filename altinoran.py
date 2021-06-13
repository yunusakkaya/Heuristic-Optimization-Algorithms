from sympy import *
import numpy as np

w= float(input("üzeri 4 olan terimin katsayısını girin:"))
a= float(input("üzeri 3 olan terimin katsayısını girin:"))
b= float(input("üzeri 2 olan terimin katsayısını girin:"))
d= float(input("üzeri 1 olan terimin katsayısını girin:"))
c= float(input("sabit terimi girin:"))

x = Symbol('x')
y = w*(x**4) + a*(x**3) + b*(x**2) + d*(x) + c

a=float(input("a yı girin:"))
b=float(input("b yi girin:"))
k=int(input("(0.618^^k*(b-a) < E) şeklinde k yı girin: :"))

for i in range (0,k+1):
    x1= b - 0.618*(b-a)
    x2= a + 0.618*(b-a)
    print("x",i+(i+1),"=",x1,", x",i+(i+2),"=",x2)
    
    if y.subs('x',x1) < y.subs('x',x2):
        a= x1
        print("yeni aralık değerleri:",a,",",b)
        print("yeni aralık:", (b-a))
        
    if y.subs('x',x1) > y.subs('x',x2):
        b= x2
        print("yeni aralık değerleri:",a,",",b)
        print("yeni aralık:", (b-a))
        
    print("_________________________________________")    
    
    
    
    



