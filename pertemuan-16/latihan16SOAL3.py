# Nested dictionary untuk data produk

produk = {
    "PROD001": {
        "nama": "Laptop",
        "harga": 7500000,
        "stok": 10
    },
    "PROD002": {
        "nama": "Smartphone",
        "harga": 3500000,
        "stok": 25
    }
}

print("Nama Produk:", produk["PROD002"]["nama"])
print("Harga Produk:", produk["PROD002"]["harga"])
