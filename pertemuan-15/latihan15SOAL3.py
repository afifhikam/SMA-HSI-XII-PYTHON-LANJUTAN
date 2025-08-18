# Latihan 3: Penggunaan .get()

biodata = {
    "nama": "Apip",
    "umur": 21,
    "hobi": ["ngoding", "membaca", "gaming"],
    "sudah_menikah": False,
    "kota": "Bandung"
}

# Coba akses key "pekerjaan" dengan bracket notation []
# print(biodata["pekerjaan"])   # <- Kalau dijalankan akan error (KeyError), makanya kita komentari

# Akses dengan .get() tanpa default
print("Akses dengan get (tanpa default):", biodata.get("pekerjaan"))

# Akses dengan .get() dengan default "Pelajar"
print("Akses dengan get (dengan default):", biodata.get("pekerjaan", "Pelajar"))
