def pirmaida_angka(number):
    for baris in range(1, number + 1):
        spasi = "  " * (number - baris)
        naik = " ".join(str(i) for i in range(1, baris + 1))
        turun = " ".join(str(i) for i in range(baris - 1, 0, -1))
        if turun:
            print(spasi + naik + " " + turun)
        else:
            print(spasi + naik)

pirmaida_angka(3)