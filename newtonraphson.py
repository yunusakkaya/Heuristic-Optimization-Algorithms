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

print("Y :", y)
print("diff of Y :", ydif)

ilknokta= float(input("start value:"))
iterasyonsayisi= int(input("iteration number :"))

for i in range(0,iterasyonsayisi+1):
    
    fonksonuc=float( y.subs('x',ilknokta))
    türevsonuc=float( ydif.subs('x',ilknokta))
    print(i,". iteration=> for function :", fonksonuc, "for diff :" ,türevsonuc)

    ilknokta=ilknokta-(fonksonuc/türevsonuc)
    print(i,".iteration result:",ilknokta) 
    print("__________________________________________")
    
