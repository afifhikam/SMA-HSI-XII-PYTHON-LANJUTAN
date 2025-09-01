# LATIHAN 6

# Buat program yang meminta pengguna memasukan umur mereka
# Program akan meminta terus untuk memasukan umur pengguna selama pengguna memasukan umur yang tidak valid
# Nilai yang valid itu 0 sampai 100, dan harus menggunakan angka bukan menggunakan huruf


   
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
