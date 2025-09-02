# LATIHAN 15

password_benar = "rahasia123"
maks_percobaan = 3

for percobaan in range(maks_percobaan):
    input_user = input("Masukkan password: ")
    if input_user == password_benar:
        print("Login berhasil!")
        break
    else:
        sisa = maks_percobaan - percobaan - 1
        print(f"Password salah. Sisa percobaan: {sisa}")
else:
    print("Akun Anda terkunci!")