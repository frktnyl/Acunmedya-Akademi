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
islem = input("İşlemi giriniz: ")

print(hesapMakinesi(sayi1, sayi2, islem))
