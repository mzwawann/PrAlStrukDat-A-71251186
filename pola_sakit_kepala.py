def pola_sakit_kepala(panjang, lebar):
    panjang = (panjang)
    lebar = (lebar)

    input(panjang, lebar)

    for i in range (number + 1):
        spasi = "  " * (number - baris)
        naik = " ".join(str(i) for i in range(1, baris + 1))
        turun = " ".join(str(i) for i in range(baris - 1, 0, -1))

print("no 1. (pola 7,7)")
pola_sakit_kepala(7, 7)
print()
print("no 2. (Pola 4, 4)")
pola_sakit_kepala(4, 4)
print()
print("no 3. (Pola -15, 15)")
pola_sakit_kepala(-15, 15)