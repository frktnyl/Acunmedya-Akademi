sayi = int(input("Bir sayı giriniz: "))
if sayi % 2 == 0:
    print("Girdiğiniz sayı çifttir.")
else:
    print("Girdiğiniz sayı tektir.")

puan = int(input("Notunuzu giriniz: "))
if puan >= 0 and puan <= 100:
    if puan >= 90:
        print("A")
    elif puan >= 80:
        print("B")
    elif puan >= 70:
        print("C")
    elif puan >= 60:
        print("D")
    else:
        print("F")
else:
    print("Geçersiz not girdiniz. Not 0 ile 100 arası olmak zorundadır.")

yas = int(input("Yaşınızı giriniz: "))
if yas <= 12:
    print("Çocuk")
elif yas <= 19:
    print("Genç")
elif yas <= 59:
    print("Yetişkin")
elif yas >= 60:
    print("Yaşlı")
else:
    print("Geçersiz yaş girdiniz.")