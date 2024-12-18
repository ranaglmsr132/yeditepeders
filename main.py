
preis=float(input("fiyat nedir:")) #Kitap fiyatı
rabatt=float(input("indirim oranı:%"))/100 #indirim oranı
kargo_1=float(input("1.kitabın kargo ücreti:"))   #1. kitabın kargo ücreti
kargo=float(input("2 ve daha fazla kitabın ücreti:"))  #2 ve daha fazla kitap kargo ücreti
zahl=float(input("kitabın fiyatı:"))
#60 kitabın fatura bedelini hesaplayın

print(((preis-preis*rabatt)*zahl)+(kargo_1+kargo*(zahl-1)))
24.95
0.4 
3
0.75
60