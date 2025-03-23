def hesapMakinesi(sayi1, sayi2, islem):
    if islem == "+":
        result = sayi1 + sayi2
        return f"İşlemin sonucu: {result} "
    
    elif islem == "-":
        result = sayi1 - sayi2
        return f"İşlemin sonucu: {result}"
    
    elif islem == "*":
        result = sayi1 * sayi2
        return f"İşlemin sonucu: {result}"
    
    elif islem == "/":
        if sayi2 == 0:
            return "Sıfıra bölme hatası!"
        else:
            result = sayi1 / sayi2
            return f"İşlemin sonucu: {result}"
    else:
        return "Geçersiz işlem!"

sayi1 = int(input("Birinci sayıyı giriniz: "))
sayi2 = int(input("İkinci sayıyı giriniz: "))
islem = input("İşlemi giriniz: \n")

print(hesapMakinesi(sayi1, sayi2, islem))

def palindromWord(word):
    if word == word[::-1]:
        return "Girilen kelime palindromdur."
    else:
        return "Girilen kelime palindrom değildir."
    
word = input("\nKelime giriniz: ")
print(palindromWord(word))

def hundredage(age):
    print(f"100 yaşına ulaşmanıza {100 - age} yıl kaldı.")

age = int(input("\nYaşınızı giriniz: "))
hundredage(age)