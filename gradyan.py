from sympy import *
import numpy as np

x1 = Symbol('x1')
x2 = Symbol('x2')

r = Symbol('r')

y = 4*x1 + 6*x2 - 2*x1**2 -2*x1*x2  -2*x2**2

ydif1 = y.diff(x1)
ydif2 = y.diff(x2)

print("fonksiyon:",y)
print("x1'e göre türevi",ydif1)
print("x2'e göre türevi",ydif2)

ilknokta1= float(input("başlangıç noktası X1:"))
ilknokta2= float(input("başlangıç noktası X2:"))

iterasyonsayisi= int(input("iterasyon sayısı girin:"))

for i in range (0,iterasyonsayisi):
    
    print(i+1,". iterasyon________________________")
    
    ydifsonuc1 = ydif1.subs('x1',ilknokta1)
    ydifsonuc1 = ydifsonuc1.subs('x2',ilknokta2)
    ydifsonuc2 = ydif2.subs('x1',ilknokta1)
    ydifsonuc2 = ydifsonuc2.subs('x2',ilknokta2)

    print("türevde yerine koyunca x1:",ydifsonuc1)
    print("türevde yerine koyunca x2:",ydifsonuc2)

    ilknokta1yeni = ilknokta1 + r*ydifsonuc1
    ilknokta2yeni = ilknokta2 + r*ydifsonuc2

    print(ilknokta1yeni,",",ilknokta2yeni)

    h = y.subs('x1',ilknokta1yeni)
    h = h.subs('x2',ilknokta2yeni)  

    print("f de yerine koyunca:",h)

    hdif = h.diff(r)

    print("h nin türevi", hdif)
    rdegeri = float(input("h yi max yapan degeri girin:"))

    ilknokta1 = ilknokta1yeni.subs('r',rdegeri)
    ilknokta2 = ilknokta2yeni.subs('r',rdegeri)

    print("X1",ilknokta1,"X2",ilknokta2)
    print("____________________________________________")



































