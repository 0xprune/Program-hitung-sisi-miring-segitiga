# Program menghitung panjang sisi miring segitiga sama kaki #
alas = input("Masukkan panjang alas : ")
tinggi = input("Masukkan panjang tinggi : ")
sisimiring = alas*alas + tinggi*tinggi
hasil = math.sqrt(sisimiring)
print("Sisi miringnya adalah : " + str(hasil))
