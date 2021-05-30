from sympy import *
import numpy as np

w= float(input("üzeri 4 olan terimin katsayısını girin:"))
a= float(input("üzeri 3 olan terimin katsayısını girin:"))
b= float(input("üzeri 2 olan terimin katsayısını girin:"))
d= float(input("üzeri 1 olan terimin katsayısını girin:"))
c= float(input("sabit terimi girin:"))

x = Symbol('x')
y = w*(x**4) + a*(x**3) + b*(x**2) + d*(x) + c
ydif = y.diff(x)

print("Y:", y)
print("Y nin türevi:", ydif)

alt=float(input("alt sınır girin:"))
üst=float(input("üst sınır girin:"))
print("aralık:",alt,üst)

iterasyonsayisi= int(input("iterasyon sayısı girin:"))

if (ydif.subs('x',alt))*(ydif.subs('x',üst)) < 0:
    
    for i in range (0,iterasyonsayisi+1):
            ortanokta= (alt+üst)/2
            print(i,".iterasyon=> şu anki orta nokta:",ortanokta)
            if ydif.subs('x',ortanokta)*ydif.subs('x',alt) < 0:
                üst=ortanokta
                print("yeni aralık:",alt,",",üst)

            if ydif.subs('x',ortanokta)*ydif.subs('x',üst) < 0:
                alt=ortanokta
                print("yeni aralık:",alt,",",üst)
                
            print("________________________________________-")
            
            
                        
      
    