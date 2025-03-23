sayiListesi = []
for i in range(5):
    sayi = int(input(f"{i+1}. sayıyı giriniz: "))
    sayiListesi.append(sayi)

#liste elemanları toplamı
total = 0
for i in sayiListesi:
    total += i

print(f"\nToplam: {total}")
print(f"Ortalama: {total/5}")
print(f"En büyük sayı: {max(sayiListesi)}")
print(f"En küçük sayı: {min(sayiListesi)}")

kelimeSayisi = int(input("\nKaç kelimeli bir liste oluşturacaksınız?\n"))
kelimeListesi = []

for i in range(kelimeSayisi):
    kelime = input(f"{i+1}. kelimeyi giriniz: ")
    kelimeListesi.append(kelime)

print(f"\nKelime listesi: {kelimeListesi}")
#tersten sıralanışı
a = kelimeListesi.reverse()
print(f"Kelime listesi tersten: {a}")

#liste içinde tekrar eden elemanları kaldıran kod
kelimeListesi = list(dict.fromkeys(kelimeListesi))
print(f"\nTekrar eden elemanlar kaldırılmış liste: {kelimeListesi}")