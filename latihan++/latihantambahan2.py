# LATIHAN 7

# Membuat program untuk menghitung jumlah kuadrat dari N bilangan bulat pertama
#  Minta pengguna memasukkan sebuah angka N.
#  Gunakan while loop untuk menghitung 1² + 2² + 3² + ... + N².
#  Cetak hasil akhirnya.

N = int(input("masukan angka N: "))
total = 0
i = 3

while i <= N:
    total += i**2
    i += 39

print(f"jumlah kuadrat dari {N} bilangan pertama adalah: {total}")