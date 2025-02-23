faiz = 1.59
vade = "36"
krediAdi = "İhtiyaç Kredisi"

print(type(faiz))
print(type(vade))
print(type(krediAdi))


print(int(vade) + 12)
#print(int(krediAdi))
faiz = str(faiz)
print(type(faiz))

vade = int(input("Lütfen istediğiniz vade sayısını girin: "))
print(type(vade))
vade = vade + 12

# string interpolation
# Seçtiğiniz vade sonucu ortaya çıkan vade:
print("Seçtiğiniz vade sonucu ortaya çıkan vade: " + str(vade))
print("Seçtiğiniz vade sonucu ortaya çıkan vade: {vadeSayisi}".format(vadeSayisi=vade))
print(f"Seçtiğiniz vade sonucu ortaya çıkan vade: {vade}")

isim = "Halit"
metin = "Merhaba {name}".format(name=123)
print(metin)


# f-string
metin = f"Hoşgeldiniz {1+1}"
print(metin)


# listeler
# döngüler
# fonksiyonlar

krediler = ["İhtiyaç Kredisi", "Konut Kredisi", "Taşıt Kredisi"]
print(type(krediler))

print(krediler[0])

print(len(krediler)) #length
# print(krediler[3]) => hata verir

krediler.append("Özel Kredi")
print(krediler)

krediler.append("X Kredisi")
print(krediler)

krediler.pop(0)
print(krediler)

krediler.append("Taşıt Kredisi")
print(krediler)


krediler.remove("Taşıt Kredisi")
print(krediler)

krediler.extend(["Y Kredisi", "Z Kredisi"])
print(krediler)

# for
# i=0 i<10

for i in range(10):
    print("xx")
    print(i)
print("****************")

for i in range(5, 11):
    print(i)
print("****************")

for i in range(0, 51, 10):
    print(i)
print("****************")

# for i in range(0.1,0.5):
#     print(i)
krediler = ["İhtiyaç Kredisi", "Konut Kredisi", "Taşıt Kredisi"]
for kredi in krediler:
    print(kredi)
print("****************")

for i in range(len(krediler)):
    print(krediler[i])
print("****************")


# sonsuz döngü
i = 0
while i < 10:
    print("x")
    i += 1
print("y")

print("****************")

while True:
    print("x")
    break

print("**** Son Döngü ****")

krediler = ["İhtiyaç Kredisi", "Konut Kredisi", "Taşıt Kredisi"]
i = 0
while i < len(krediler):
    i += 1
    print(i)
    print(krediler[i])
    if krediler[i] == "Konut Kredisi":
        break

# fonksiyonlar

fiyat = 100
indirim = 20
#definition define
def calculate():
    print(100-20)

def calculateWithParams(fiyat, indirim):
    print(fiyat - indirim)

def sayHello(name):
    print(f"Merhaba {name}")


calculate()
calculateWithParams(50, 10)
calculateWithParams(100, 30)
sayHello("Halit")
sayHello("Arif")
sayHello("Mevlüt")


def calculateAndReturn(price, discount):
    return price-discount

yeniFiyat = calculateAndReturn(200, 50)
print(yeniFiyat + 10)


def calculatePrice(price, discount):
    print(price - discount)

def calculatePriceAndReturn(price, discount):
    return price - discount

print("**************")
fonk1 = calculatePrice(100, 50)
fonk2 = calculatePriceAndReturn(300, 100)
print(f"157.satır: {fonk1}")
print(f"158.satır: {fonk2}")
print("**************")

# sınıflar
# modules
# paket yönetimi

class Human:
    #built-in #constructor #initialize
    def __init__(self, name):
        self.name = name
        print("Bir insan instance'ı üretildi.")
    def talk(self, sentence):
        print(f"{self.name}: {sentence}")
    def walk(self):
        print(f"{self.name} is walking...")

# instance -> örnek
human1 = Human()
human1.name = "Enes"
human1.talk("Merhaba")
human1.walk()
print(human1)


human2 = Human()
human2.name = "Cem"
human2.talk("Selam")
human2.walk()
print(human2)

