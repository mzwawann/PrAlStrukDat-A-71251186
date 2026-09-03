def pirmaida_angka(angka):
    for baris in range(1, angka + 1):
        spasi = "  " * (angka - baris)
        naik = " ".join(str(i) for i in range(1, baris + 1))
        turun = " ".join(str(i) for i in range(baris - 1, 0, -1))
        if turun:
            print(spasi + naik + " " + turun)
        else:
            print(spasi + naik)

pirmaida_angka(3)