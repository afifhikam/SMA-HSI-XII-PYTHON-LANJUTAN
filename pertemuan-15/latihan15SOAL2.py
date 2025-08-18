# Latihan 2: Modifikasi Dictionary

# Dictionary biodata dari Latihan 1
biodata = {
    "nama": "Apip",
    "umur": 20,
    "hobi": ["ngoding", "membaca", "gaming"],
    "sudah_menikah": False
}

# Tambahkan key-value baru: "kota"
biodata["kota"] = "Bandung"

# Ubah value dari key "umur" menjadi umur tahun depan
biodata["umur"] = biodata["umur"] + 1

# Cetak dictionary yang sudah diperbarui
print("Dictionary setelah diperbarui:", biodata)
