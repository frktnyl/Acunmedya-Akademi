#Görev 1 ve 2

metin = input("Enter a text: ")

with open("metin.txt", "w") as file:
    file.write(metin)

with open("metin.txt", "r") as file:
    metin = file.read()

print(f"\nMetin içeriği = {metin}")

#Görev 3

with open("satirlar.txt", "w") as file:
    for i in range(5):
        satir = input(f"\n{i+1}. satırın içeriğini giriniz: ")
        file.write(satir + "\n")
    print("\n5 satır oluşturuldu.\n")

with open("satirlar.txt", "r") as file:
    satirlar = file.readlines()
    for i in range(5):
        print(f"{i+1}. satır: {satirlar[i]}")
