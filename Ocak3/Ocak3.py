def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

for i in range(1,101):
    print(i)

for i in range(2,101,2):
    print(i)

sayi = int(input("Bir sayı giriniz: "))
factorial_sayi = factorial(sayi)
print(f"{sayi}! = {factorial_sayi}")

#asal sayı
for i in range(1,101):
    if i > 1:
        for j in range(2,i):
            if i % j == 0:
                break
        else:
            print(i)