import numpy as np # nümerik işlemler için
import random # rastgelelik için
import matplotlib.pyplot as plt # grafikler için

n=7 # uğranacak şehir/durak sayısı 

alfa=0.5 # alfa 
beta=0.5 # beta
rho=0.001 # buharlaşma parametresi

# veri girisi
sehirtablo=np.array([[0,3313,2963,3175,3339,2762,3276],[3313,0,1318,1326,1294,1498,2218],[2963,1318,0,204,583,206,966],[3175,1326,204,0,460,409,1136],[3339,1294,583,460,0,785,1545],[2762,1498,206,409,785,0,760],[3276,2218,966,1136,1545,760,0]],dtype=float)
sehirtablo=sehirtablo.reshape(n,n) # tablo formuna getirme

feromon_tablo=np.array([[0]*n]*n,dtype=float) # feromon miktarları için tablo oluştur
feromon_tablo = feromon_tablo.reshape(n,n) # tabloyu şekillendir

# olasılık tablosu oluştur (baştaki olasılıklar eşit)
p_tablo=np.array([[0, 0.16, 0.16, 0.16, 0.16, 0.16, 0.16],[0.16, 0, 0.16, 0.16, 0.16, 0.16, 0.16],[0.16, 0.16, 0, 0.16, 0.16, 0.16, 0.16],[0.16, 0.16, 0.16, 0, 0.16, 0.16, 0.16],[0.16, 0.16, 0.16, 0.16, 0, 0.16, 0.16],[0.16, 0.16, 0.16, 0.16, 0.16, 0, 0.16],[0.16, 0.16, 0.16, 0.16, 0.16, 0.16, 0]],dtype=float)
p_tablo = p_tablo.reshape(n,n) # tabloyu şekillendir

bestof=[] # iterasyon sonu değerleri buraya kaydedilecek
           
print("ŞEHİRLER ARASI MESAFELER:\n",sehirtablo) # mesafe tablosunu gösterme
olasılık= True # döngüde kullanılacak giriş şartı

for a in range(50): # iterasyon başlangıcı
    rotalist=[] # rotalar kaydedilecek
    mesafelist=[] # mesafeler kaydedilecek
    
    for w in range(n): # her karınca için gidiş oluşacak
        rota=[] # gidiş yolu eklenecek
        i=random.randrange(0,n,1) # Rastgele komşu seçenek ve ilk deger oluşturma
        j=random.randrange(0,n,1) # ilk gidilecek yer
        j_list=[] # daha önce gidilen yer kayıt edilecek
        mesafe=0 # mesafe uzunluğu kaydedilecek
        
        
        
                
        
        while (len(rota)+1 <= n-1): # Bütün şehirlere gidince döngü duracak
    
            j=random.randrange(0,n,1) # döngü boyunca oluşacak gidişler
            
            if feromon_tablo[i,j]!=0: # feromon yoksa eksiltme
                feromon_tablo[i,j]=feromon_tablo[i,j] -rho # buharlaşma işlemini gerçekleştir
                            
            if i != j and (j not in j_list) and olasılık == True : # daha önce gidilmişse gitme          
                
                mesafe = mesafe + sehirtablo[i,j] # bir rotanın mesfesi
                feromon_tablo[i][j] = feromon_tablo[i][j] + 0.1 # her karınca geçtiğinde yolda feromon artacak
                gidis=str(i+1),str(j+1) # nereden nereye
                rota.append(gidis) # rotayı liste şeklinde sakla
                                       
                j_list.append(i) # ilk yeri kaydet ve tekrar gitme
                i=j # gidilen yer artık bulunulan yer
                j_list.append(j) # gidilen yeri kaydet ve tekrar gitme
                
      
        k_toplam=[0]*n # olasılık hesabındaki kümülatif toplam

        for i in range(n): # hesaptaki toplam kısmı için döngü
             for j in range(n): # satır sütün değişimi
                 k_toplam[i] = k_toplam[i] + (feromon_tablo[i,j]**alfa)*(sehirtablo[i,j]**beta) # toplamı hesapla

        for i in range(0,n): # olasılık tablosu oluşturma/güncelleme
             for j in range(0,n): # satır sütün değişimi için
                 p_tablo[i,j] =((feromon_tablo[i,j]**alfa)*(sehirtablo[i,j]**beta))/(k_toplam[i]) # olasılık formülü hesaplama
                 p_tablo[i,j]= round(p_tablo[i,j],2) # virgülden sonra 2 basamak al      
                
                
                
            
        
                
        rotalist.append((rota))   # rotaları kaydet                     
        mesafelist.append(mesafe) # mesafeleri kaydet
        print("------------------------------------------------------------")   # süs
        print("rota",w+1,":",rota) # şu anki rotayı göster
        print("----------------------------------------------------------------") # süs

        
        
    print("mesafeler:",mesafelist) # iterasyon sonunda her karıncanın aldığı yol uzunluğunu göster
    print("----------------------------------------------------------------") # süs
    print("olasılık dağılımı") # başlık
    print(p_tablo) # olasılık tablosunu göster
    print("----------------------------------------------------------------") # süs
    print("feromon miktarları:") # başlık
    print(feromon_tablo) # feromon miktarlarını göster
    print("----------------------------------------------------------------") # süs
    
    print(a +1,". iterasyon en iyi rota:",min(rotalist)) # en iyi rotayı göster
    print("----------------------------------------------------------------") # süs
    print(a +1,". iterasyon en iyi mesafe:",min(mesafelist)) # en kısa mesafeyi göster
    print("----------------------------------------------------------------") # süs
    olasılık = p_tablo[i,j] <= random.random() # bir sonraki iterasyonda yol seçimi için olasılık belirle
    
    bestof.append(min(mesafelist)) # her iterasyondaki en kısa mesafeyi kaydet
    
plt.plot(bestof) # her iterasyondaki en kısa mesafeyi al grafiğini çiz
plt.title("mesafe grafiği") # başlık
plt.xlabel("iterasyon") # başlık
plt.ylabel("mesafe") # başlık
plt.show() # grafiği göster
    
    