menu = {
    "1": {"isim": "Kebap", "fiyat": 120},
    "2": {"isim": "Lahmacun", "fiyat": 50},
    "3": {"isim": "İskender", "fiyat": 130},
    "7": {"isim": "Künefe", "fiyat": 45},
    "10": {"isim": "Çay", "fiyat": 10},
    "4": {"isim": "Makarna", "fiyat": 225},
    "5": {"isim": "Pizza", "fiyat": 145},
    "6": {"isim": "Hamburger", "fiyat": 200},
    "8": {"isim": "Baklava", "fiyat": 100},
    "9": {"isim": "Sütlaç", "fiyat": 225},
    "11": {"isim": "Kola", "fiyat": 90},
    "12": {"isim": "Ayran", "fiyat": 70},

}

def menugosterme():
    print("\n--- MENÜ ---")

    print("\n-- Yemekler --")
    print("1. Kebap - 120 TL")
    print("2. Lahmacun - 50 TL")
    print("3. İskender - 130 TL")
    print("4. Makarna - 225 TL")
    print("5. Pizza - 145 TL")
    print("6. Hamburger - 200 TL")

    print("\n-- Tatlılar --")
    print("7. Künefe - 45 TL")
    print("8. Baklava - 100 TL")
    print("9. Sütlaç - 225 TL")

    print("\n-- İçecekler --")
    print("10. Çay - 10 TL")
    print("11. Kola - 90 TL")
    print("12. Ayran - 70 TL")

def siparis():
    sepet = []
    while True:
        secim = input("Lütfen ürün numarası girin (çıkmak için q): ")
        if secim == "q":
            break
        elif secim in menu:
            sepet = sepet + [menu[secim]]  
            print(menu[secim]["isim"] + " sepete eklendi.")
        else:
            print("Geçersiz seçim.")
    return sepet

def odeme(sepet):
    toplam = 0
    for urun in sepet:
        toplam += urun["fiyat"]
    print("Toplam tutar:", toplam, "TL")

    odemeyontemi = input("Ödeme yöntemi (nakit/kredi kartı): ")

    if odemeyontemi == "nakit":
        odeme = input("Ödenen miktar: ")
        try:
            odeme = float(odeme)
            if odeme >= toplam:
                print("Ödeme başarılı. Para üstü:", odeme - toplam, "TL")
                print("Afiyet olsun!")
            else:
                print("Yetersiz ödeme.")
        except:
            print("Geçerli bir sayı girin.")

    elif odemeyontemi == "kredi kartı":
        sifre = input("Şifreyi girin: ")
        if sifre == "1234":
            print("Ödeme başarılı. Afiyet olsun!")
        else:
            print("Yanlış şifre.")
    else:
        print("Geçersiz ödeme yöntemi.")

def robotmenu():
    print(" Restoran'a Hoş Geldiniz!")
    menugosterme()
    sepet = siparis()
    if len(sepet) == 0:
        print("Sepet boş. Görüşmek üzere.")
    else:
        print("\n--- Sipariş Özeti ---")
        for urun in sepet:
            print("- " + urun["isim"] + " (" + str(urun["fiyat"]) + " TL)")
        odeme(sepet)

robotmenu()
