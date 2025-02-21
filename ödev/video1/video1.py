# Python Ödevi

# 1️⃣ Kullanıcıdan isim ve yaş alıp mesaj yazdırma
isim = input("Adınızı girin: ")
yaş = int(input("Yaşınızı girin: "))

print(f"Merhaba {isim}, yaşınız {yaş}!")

# 2️⃣ Temel matematiksel işlemler
a = int(input("Birinci sayıyı girin: "))
b = int(input("İkinci sayıyı girin: "))

toplam = a + b
fark = a - b
çarpım = a * b
bölüm = a / b

print(f"Toplam: {toplam}, Fark: {fark}, Çarpım: {çarpım}, Bölüm: {bölüm}")

# 3️⃣ Mantıksal operatörlerle erişim kontrolü
if yaş >= 18:
    print("Erişime izin verildi.")
else:
    print("Erişime izin verilmedi.")

# 4️⃣ Mantıksal operatörler örneği (and, or)
parola = input("Parolanızı girin: ")
if len(parola) >= 8 and "123" not in parola:
    print("Parola geçerli.")
else:
    print("Parola zayıf, lütfen tekrar girin.")
