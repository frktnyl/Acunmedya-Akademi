def asal_mi(sayi):

    if sayi <= 1 or sayi % 2 == 0:
        return f"{sayi} asal sayı değildir."

    if sayi == 2:
        return f"{sayi} asal sayıdır."

    for bölen in range(2, int(sayi ** 0.5) + 1, 2):   
        if sayi % bölen == 0:
            return f"{sayi} asal sayı değildir."
        
    return f"{sayi} asal sayıdır."

sayi  = int(input("Sayıyı giriniz: "))
print(asal_mi(sayi))
