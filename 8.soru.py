def harfler():
  kelime=input("Sözcük Giriniz: ")
  harf=input("Harf Giriniz: ")
  sayi=0
  
  for h in kelime:
    if h==harf:
      sayi+=1
  print(sayi)
  
harfler()












