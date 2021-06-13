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

ilknokta= float(input("başlangıç noktası girin:"))
iterasyonsayisi= int(input("iterasyon sayısı girin:"))

for i in range(0,iterasyonsayisi+1):
    
    fonksonuc=float( y.subs('x',ilknokta))
    türevsonuc=float( ydif.subs('x',ilknokta))
    print(i,". iterasyon=> fonksiyon için:", fonksonuc, "türev için:" ,türevsonuc)

    ilknokta=ilknokta-(fonksonuc/türevsonuc)
    print(i,".iterasyon sonucu:",ilknokta) 
    print("__________________________________________")
    