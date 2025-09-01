# LATIHAN 6

# Tujuan singkat: minta umur, ulang terus sampai inputnya angka dan masuk akal (0–100).
# Langkah step-by-step:
# Mulai loop while True supaya program terus minta input sampai valid.
# Minta input dari user (input()), hasilnya string.
# Coba konversi string ke int dengan int(...).
# Kalau konversi gagal, akan muncul ValueError → tangkap dengan except dan beri pesan "Input tidak valid".
# Kalau berhasil jadi integer, cek apakah di rentang 0–100. Kalau tidak, beri pesan "Umur tidak wajar" dan loop lanjut.
# Kalau valid, print umur dan break keluar dari loop.
# Contoh kode (komentar jelasin tiap baris):

   
while True:
    try:
        umur = int(input("masukan umur anda: "))
        if umur < 0 or umur > 100:
            print("umur kamu tua banget, disini umurnya 100 tahun ke bawah")
        else:
            print(f"termia kasih umur anda adalah {umur}.")
            break
    except ValueError:
        print("kamu gak bisa baca? ")
