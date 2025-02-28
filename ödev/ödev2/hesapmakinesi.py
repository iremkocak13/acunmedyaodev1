def hesap_makinesi(sayi1, sayi2, islem):
    if islem == '+':
        return sayi1 + sayi2
    elif islem == '-':
        return sayi1 - sayi2
    elif islem == '*':
        return sayi1 * sayi2
    elif islem == '/':
        if sayi2 == 0:
            return "Bölme işlemi için ikinci sayı 0 olamaz!"
        else:
            return sayi1 / sayi2
    else:
        return "Geçersiz işlem türü!"

# Kullanıcıdan giriş alma
sayi1 = float(input("Birinci sayıyı girin: "))
sayi2 = float(input("İkinci sayıyı girin: "))
islem = input("Yapmak istediğiniz işlemi girin (+, -, *, /): ")

# Sonucu hesapla ve yazdır
sonuc = hesap_makinesi(sayi1, sayi2, islem)
print("Sonuç:", sonuc)