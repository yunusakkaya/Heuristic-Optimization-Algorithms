import numpy as np # nümerik işlemler için
import random # rastgelelik için
import matplotlib.pyplot as plt # grafikler için

n=7 # uğranacak şehir/durak sayısı 

# veri girisi
sehirtablo=np.array([[0,3313,2963,3175,3339,2762,3276],[3313,0,1318,1326,1294,1498,2218],[2963,1318,0,204,583,206,966],[3175,1326,204,0,460,409,1136],[3339,1294,583,460,0,785,1545],[2762,1498,206,409,785,0,760],[3276,2218,966,1136,1545,760,0]],dtype=float)
sehirtablo=sehirtablo.reshape(n,n) # tablo formuna getirme
                       
print("ŞEHİRLER ARASI MESAFELER:\n",sehirtablo) # mesafe tablosunu gösterme

bestof_rota=[] # çaprazlamada kullanılacak 
bestof_mesafe=[] # çaprazlamada kullanılacak

for a in range(10): # grupları oluşturmaya başlıyoruz
    print("--------------------------------------------------------------------") # süs
    print("İTERASYON NO:",a + 1)                                                     # kaçıncı popülasyon 
    print("--------------------------------------------------------------------") # süs
    mesafelist=[] # mesafeleri karşılaştırmak için
    rotalist=[] # rotaları seçebilmek için
    
    for w in range(100): 
        rota=[] 
        i=random.randrange(0,n,1) # Rastgele komşu seçenek ve ilk deger oluşturma
        j=random.randrange(0,n,1)
        mesafe=0
        j_list=[] 
        

        while (len(rota)+1 <= n-1): # Bütün şehirlere gidince döngü duracak
        
            j=random.randrange(0,n,1) # döngü boyunca oluşacak gidişler         
        
            if  sehirtablo[i,j]!=0 and j not in j_list : # daha önce gidilmişse gitme          
        
                mesafe = mesafe + sehirtablo[i,j] # bir rotanın mesfesi
                gidis=str(i),str(j) # nereden nereye
                rota.append(gidis) # rotayı liste şeklinde sakla
                j_list.append(i) # ilk yeri kaydet ve tekrar gitme
                i=j # gidilen yer artık bulunulan yer
                j_list.append(j) # gidilen yeri kaydet ve tekrar gitme

        rotalist.append((rota))   # rotaları kaydet                     
        mesafelist.append(mesafe) # mesafeleri kaydet
        print("------------------------------------------------------------")   # süs
        print("rota",w+1,":",rota) # şu anki rotayı göster
    
    
    print("----------------------------------------------------------------") #süs
    print("mesafe:",mesafelist) # mesafeleri göster

    min_mesafe= min(mesafelist) # en kısa mesafeyi kaydet
    print("minimum mesafe:" ,min_mesafe)  # en kısa mesafeyi göster
    print("en iyi seçenek: rota", mesafelist.index(min_mesafe)+1) # en kısa mesafenin olduğu rotaynın numarasını göster
    print(rotalist[mesafelist.index(min_mesafe)]) # en iyi rotanın kendisini göster

    plt.plot(mesafelist) # mesafeleri grafiğe dök
    plt.title(str(a+1) + ". iterasyon Sonuçları Grafiği:") # başlık
    plt.xlabel("rota numarası (iterasyon içinde kaçıncı rota?)") # x ekseni ismi
    plt.ylabel("rota sonucu oluşan mesafe") # y ekseni ismi
    plt.show() # grafiği göster
    
    bestof_mesafe.append(min_mesafe) # bütün grupların en iyi mesafelerini kaydet
    bestof_rota.append(rotalist[mesafelist.index(min_mesafe)]) # en iyi rotaları kaydet
    

print("Best of Rota:")    # başlık 
for b in range(len(bestof_rota)): # rota listesinin uzunluğu kadar dön
    print(bestof_rota[b]) # sıra sıra en iyi rotaları göster
    
print("Best of Mesafe:")   # başlık 
for c in range(len(bestof_mesafe)): # mesafe listesinin uzunluğu kadar dön
    print(bestof_mesafe[c]) # sıra sıra en iyi mesafeleri göster
    
cross_list=[]    # çaprazlamaları kaydetmede kullanılacak
çaprazlama_olasılık= 0.7 # çaprazlama olasılık sınırı (ilk adımı atması için başta 0.7 veriliyor)

while (len(cross_list)!=10): # çaprazlama sayısı belli bir sayı olana kadar dön
         
    yarı_1=[] # kromotit 1
    yarı_2=[] # kromotit 2
    r1=random.randrange(0,n,1) # listenin içinden rastgele bir rota numarası seç
    r2=random.randrange(0,n,1) # listenin içinden rastgele bir rota numarası daha seç 
    yarı_1=(bestof_rota[r1][0:3])   # birini ilk kromotite koy
    yarı_2=(bestof_rota[r2][3:6])   # diğerini diğer kromotite koy

        
    mutasyon=random.randrange(0,1) # mutasyon olasılıgı
    
    if mutasyon <= 0.001: # eğer mutasyon olasığı şundan az ise aşağıdaki işlemi yap
        
        yarı_1 , yarı_2 = yarı_2 , yarı_1    # kromotitlerin yerini değiştir    
    
    if çaprazlama_olasılık >= 0.7: # olasılık sağlanıyorsa yap
        ilk_i= yarı_1[0][0] # ilk rotanın başlangıcını kaydet ki tekrar gitme
        for i in range(0,len(yarı_1)): # ilk kromotititin elemanlarında gez
            for j in range(len(yarı_1[i])): # o sıradaki elemanın rotasında gez
                for k in range(len(yarı_2)): # ikinci kromotitin elemanlarında gez
                    for t in range(len(yarı_2[k])):  # o sıradaki elemanın rotasında gez
                        if yarı_2[k][1]!= yarı_1[i][1] and yarı_2[k][1]!= ilk_i and yarı_2[0][0]== yarı_1[2][1]: # gideceğin yer daha önce gitmediğin yer olsun ve ilk yarının sonu ikincinin başlangıcı olsun
                            cross= yarı_1 + yarı_2 # şartları sağlayan kromotitleri birleştir ve kromozomu oluştur
                            if cross not in cross_list: # bu olasılık daha önce eklenmediyse 
                                cross_list.append(cross) # çaprazlama sonuçlarına ekle
    else: #olasılık sağlanmıyorsa önceki sonuçla devam et 
        cross= yarı_1 + yarı_2 # şartları sağlayan kromotitleri birleştir ve kromozomu oluştur
        cross_list.append(cross) # çaprazlama sonuçlarına ekle
    çaprazlama_olasılık= random.randrange(0,1) # yeni olasılık oluştur    
                            
                        
   
print("Çaprazlama Sonuçları:") # başlık
for p in range(len(cross_list)): # çaprazlama listesi kadar dön
    print(cross_list[p])    # sıra sıra elemanlarını yazdır
    print("--------------------------------------------------------------------") # süs
 
cross_mesafe_list=[]    # çaprazlama sonucu oluşan mesafeleri kaydetmek için kullanılacak
for i in range (0,10): # 10 kere dön
    cross_mesafe=0 # mesafeyi kaydetmek için
    for j in range (0,6): # 6 kere dön (gidiş sayısı 6 olduğu için)
    
        cross_i=int(cross_list[i][j][0]) # çaprazlama sonuçlarının yola çıkacağı yer
        cross_j=int(cross_list[i][j][1]) # çaprazlama sonuçlarının gideceği yer
        
        cross_mesafe= cross_mesafe + sehirtablo[cross_i][cross_j] # bu gidiş için mesafeyi tablodan al ve ekle
    cross_mesafe_list.append(cross_mesafe) # oluşan mesafeyi kaydet
print("Çaprazlanmış mesafeler:")        # başlık
for y in range (len(cross_mesafe_list)): # mesafe listesi kadar dön
    print(cross_mesafe_list[y])  # elemanlarını sıra sıra yazdır
    
print("en iyi sonuç:",min(cross_mesafe_list),"en iyi rota:",cross_list[cross_mesafe_list.index(min(cross_mesafe_list))] )   # en iyi mesafeyi ve en iyi rotayı index sırasına göre bul ve yazdır 
cross_mesafe_list.sort(reverse=True)
plt.title("En İyi Mesafe Grafiği:") # başlık
plt.xlabel("iterasyon numarası") # x ekseni ismi
plt.ylabel("iterasyon içindeki en iyi sonuç (mesafe)") # y ekseni ismi

plt.plot(cross_mesafe_list,"r") # çaprazlama sonuçlarının mesafelerini grafiğe dök
plt.show() # grafiği göster



        
        
        
        
        
        
        
        
        
    
    
    
    
