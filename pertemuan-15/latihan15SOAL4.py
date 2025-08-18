# Latihan 4: Histogram Kata

# Meminta input kalimat dari pengguna
kalimat = input("Masukkan sebuah kalimat: ").lower()   # ubah ke lowercase biar konsisten

# Ubah kalimat jadi list kata-kata
kata_list = kalimat.split()

# Buat dictionary histogram
histogram = {}

for kata in kata_list:
    histogram[kata] = histogram.get(kata, 0) + 1   # hitung frekuensi kata

# Cetak hasil histogram
print("Histogram kata:", histogram)
