# LATIHAN 9
# Mulai dari angka 2 (1 bukan prima).
# Pakai loop luar while sampai nemu 5 prima.
# Set “bendera” prima = True.
# Cek pembagi dari 2 sampai angka-1. Kalau ada yang habis dibagi, set prima = False dan break.
# Kalau prima masih True, print angkanya dan tambah hitungan jumlah prima.

# Naikkan angka dan ulangi.

jumlah_prima = 0
angka = 2

while jumlah_prima < 5:
    prima = True
    for pembagi in range(2, angka):
        if angka % pembagi == 0:
            prima = False
            break
    if prima:
        print(angka)
        jumlah_prima += 1
    angka += 1
