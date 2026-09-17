import random
def presensi_dummy(data):
    for i in data:
        i.append(random.randint(70,100))

def acak_data(data):
    random.shuffle(data)

def show_data(data):
    width = 52
    print("="*width)
    print(f"|{'NIM':^10}|{'Nama':^30}|{'Presensi':^5}|")
    print("="*width)
    for i in data:
        nama = i[1].split(" ")
        print(f"|{i[0]:^10}|{' '.join(nama[:3]):^30}|{i[2]:^8}|")
    print("="*width)