# ==============================
# Latihan 1: Membuat dan Mengakses
# ==============================
biodata = {
    "nama": "Apip",
    "umur": 20,
    "hobi": ["ngoding", "membaca", "gaming"],
    "sudah_menikah": False
}

print("Dictionary biodata:", biodata)               # Cetak seluruh dictionary
print("Nama:", biodata["nama"])                     # Cetak value dari key "nama"
print("Hobi pertama:", biodata["hobi"][0])          # Cetak hobi pertama dari list

# ==============================
# Latihan 2: Modifikasi Dictionary
# ==============================
biodata["kota"] = "Bandung"                         # Tambah key-value baru
biodata["umur"] = biodata["umur"] + 1               # Ubah umur jadi tahun depan
print("\nDictionary setelah update:", biodata)

# ==============================
# Latihan 3: Penggunaan .get()
# ==============================
# print(biodata["pekerjaan"])  # <- baris ini kalau dijalankan akan error (KeyError)
print("\nAkses dengan get (tanpa default):", biodata.get("pekerjaan"))  
print("Akses dengan get (dengan default):", biodata.get("pekerjaan", "Pelajar"))

# ==============================
# Latihan 4: Histogram Kata
# ==============================
kalimat = input("\nMasukkan sebuah kalimat: ").lower()   # Ubah ke lowercase
kata_list = kalimat.split()                              # Pisahkan jadi list kata
histogram = {}

for kata in kata_list:
    histogram[kata] = histogram.get(kata, 0) + 1         # Hitung frekuensi kata

print("\nHistogram kata:", histogram)
