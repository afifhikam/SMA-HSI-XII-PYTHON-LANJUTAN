# Dictionary kosong untuk kontak

kontak = {}

kontak["Ibu"] = "08123456789"
kontak["Ayah"] = "08987654321"
kontak["Teman"] = "082233445566"

print("Kontak awal:", kontak)

kontak["Ibu"] = "08111111111"

kontak.pop("Teman")

print("Kontak akhir:", kontak)
