# Latihan 3:

biodata = {
    "nama": "Apip",
    "umur": 21,
    "hobi": ["ngoding", "membaca", "gaming"],
    "sudah_menikah": False,
    "kota": "Bandung"
}

print("Akses dengan get (tanpa default):", biodata.get("pekerjaan"))

print("Akses dengan get (dengan default):", biodata.get("pekerjaan", "Pelajar"))
