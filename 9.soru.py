metin=input("Metin Giriniz: ")
kelime=input("Kelime Giriniz: ")

yeni = ""

for harf in metin:
    if harf not in kelime:
        yeni+= harf

print( yeni)











