# Kullanıcının girdiği metni bir .txt dosyasına yazma
with open("metin_dosyasi.txt", "w", encoding="utf-8") as dosya:
    metin = input("Bir metin girin: ")
    dosya.write(metin)

# Dosyanın içeriğini okuma ve ekrana yazdırma
with open("metin_dosyasi.txt", "r", encoding="utf-8") as dosya:
    icerik = dosya.read()
    print("\nDosya İçeriği:")
    print(icerik)

# Kullanıcıdan alınan 5 farklı satırı dosyaya kaydetme
with open("satirlar_dosyasi.txt", "w", encoding="utf-8") as dosya:
    print("\n5 farklı satır girin:")
    for i in range(5):
        satir = input(f"Satır {i+1}: ")
        dosya.write(satir + "\n")

# Dosyanın içeriğini satır satır okuma ve ekrana yazdırma
with open("satirlar_dosyasi.txt", "r", encoding="utf-8") as dosya:
    print("\nDosyadaki Satırlar:")
    for satir in dosya:
        print(satir.strip())
