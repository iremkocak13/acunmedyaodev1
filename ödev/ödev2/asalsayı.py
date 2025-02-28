def asal_mi(sayi):
    if sayi < 2:
        return f"{sayi} bir asal sayı değildir."
    for i in range(2, int(sayi ** 0.5) + 1):
        if sayi % i == 0:
            return f"{sayi} bir asal sayı değildir."
    return f"{sayi} bir asal sayıdır."

# User input section
try:
    sayi = int(input("Bir sayı girin: "))
    print(asal_mi(sayi))
except ValueError:
    print("Lütfen geçerli bir sayı girin.")