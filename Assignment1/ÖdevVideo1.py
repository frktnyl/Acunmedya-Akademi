print("Kodlamaio")
baslik = "Taşıt Kredisi"
print(baslik)

#String -> Metinsel ifadeler
baslik = "İhtiyaç Kredisi"
print(baslik)

#Integer -> Tam sayılar
vade = 36
ekvade = 6
vade2 = "36"

#Float -> Ondalıklı sayılar
aylikOdeme = 200.50

#Boolean -> True/False
yukselisteMi = False

#Matematiksel İşlemler
# +
print(5 + 5)
print(vade + 12)
print(vade + ekvade)
print(36 + 6)

# -
print(5 - 5)
print(vade - 12)
print(vade - ekvade)
print(36 - 6)

# *
print(5 * 5)
print(vade * 12)
print(vade * ekvade)
print(10 * 10)

# /
print(5 / 5)
print(vade / 12)
print(vade / ekvade)
print(10 / 2)

yeniVade = vade / 2
fiyat = 100
indirimliFiyat = fiyat - 20

print(yeniVade)
print(indirimliFiyat)

#mod operatörü
print(10 % 2)
print(vade % 2)
print(vade % ekvade)
print(30 % 10)

#mantıksal operatörler
print(5 == 5)
print(5 == 6)

# CTRL K + CTRL C
print(1 > 2)
print(3 > 1)
print(1 > 1)
print(1 >= 1)

print(1 < 2)
print(3 < 1)
print(1 < 1)
print(1 <= 1)

print(1 != 1)
print(1 != 2)

# or and

# or -> veya
print(1 > 2 or 5 > 2)
print(1 > 2 and 5 > 2)
print(1 > 2 or 5 > 2 and 3 > 2)

print(1 > 2 and 5 > 2 and 3 > 2)

print(2 > 1 or 1 > 2 or 3 > 2)

# karar yapıları
# if else
sayi1 = 10
sayi2 = 15
#sayi1 sayi2'den büyükse ekrana sayi 1 daha büyük yazdır
#condition

#indent
if sayi1 > sayi2:
    print("Sayı 1 daha büyük")
    print("Hala if bloğu içindeyim")
#eğer if bloğuna girmez ise
elif sayi1 == sayi2:
    print("Sayılar eşit")
#eğer if ve elif bloklarına girmez ise
else:
    print("Sayı 1 sayi 2'den küçüktür")

print("if bloğu bitti")