kelime=input("Kelime Giriniz: ")
harf=input("Harf Giriniz: ")

thistuple = ("a","e","u","ı","i","ü","ö","o")
sayac=0

for sesli in kelime :
    if harf in thistuple and sesli==harf :
        sayac+=1
        
print(sayac)












