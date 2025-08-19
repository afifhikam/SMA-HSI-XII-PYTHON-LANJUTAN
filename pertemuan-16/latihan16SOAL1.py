# Dictionary 

harga_buah = {"apel": 5000, "jeruk": 8500, "mangga": 7800, "pisang": 3000}

total_harga = 0

for buah, harga in harga_buah.items():
    print(f"Harga 1 kg {buah} adalah Rp {harga}")
    total_harga += harga  

print(f"Total harga semua buah adalah Rp {total_harga}")
