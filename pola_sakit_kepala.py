def pola_sakit_kepala(panjang, lebar):
   
    panjang = abs(panjang)
    lebar = abs(lebar)

    if panjang != lebar:
        print("Panjang dan lebar harus sama!!")
    elif panjang % 2 == 0:
        print("Panjang dan lebar harus bilangan ganjil!!")
    else:
        n = panjang
        tengah = n // 2   

        for baris in range(n):
            for kolom in range(n):
                # jarak Manhattan dari titik tengah + 1 = nilai pada posisi itu
                jarak = abs(baris - tengah) + abs(kolom - tengah)
                nilai = (jarak + 1) % 10  

                if kolom == n - 1:
                    print(nilai, end="")
                else:
                    print(nilai, end=" ")
            print()


print("no 1. (pola 7,7)")
pola_sakit_kepala(7, 7)
print()
print("no 2. (Pola 4, 4)")
pola_sakit_kepala(4, 4)
print()
print("no 3. (Pola -15, 15)")
pola_sakit_kepala(-15, 15)