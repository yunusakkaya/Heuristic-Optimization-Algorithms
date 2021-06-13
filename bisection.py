from sympy import *
import numpy as np

w= float(input("Term coefficient with 4 power of x:"))
a= float(input("Term coefficient with 3 power of x:"))
b= float(input("Term coefficient with 2 power of x:"))
d= float(input("Term coefficient with 1 power of x:"))
c= float(input("constant term:"))

x = Symbol('x')
y = w*(x**4) + a*(x**3) + b*(x**2) + d*(x) + c
ydif = y.diff(x)

print("Y:", y)
print("Diff of Y:", ydif)

alt=float(input("lower variable:"))
üst=float(input("upper variable:"))
print("aralık:",alt,üst)

iterasyonsayisi= int(input("number of iteration:"))

if (ydif.subs('x',alt))*(ydif.subs('x',üst)) < 0:
    
    for i in range (0,iterasyonsayisi+1):
            ortanokta= (alt+üst)/2
            print(i,".iterasyon=> şu anki orta nokta:",ortanokta)
            if ydif.subs('x',ortanokta)*ydif.subs('x',alt) < 0:
                üst=ortanokta
                print("new range:",alt,",",üst)

            if ydif.subs('x',ortanokta)*ydif.subs('x',üst) < 0:
                alt=ortanokta
                print("new range:",alt,",",üst)
                
            print("________________________________________-")
            
            
                        
      
    
