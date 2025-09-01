# LATIHAN 8

kalimat = input("Masukkan kalimat: ")
hasil = ""

for huruf in kalimat:
    if huruf.lower() in "aiueo":
        continue
    hasil += huruf

print(hasil)
