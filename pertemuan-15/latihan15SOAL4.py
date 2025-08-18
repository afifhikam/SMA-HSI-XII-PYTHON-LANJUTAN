# Latihan 4: 

kalimat = input("Masukkan sebuah kalimat: ").lower()   

kata_list = kalimat.split()

histogram = {}

for kata in kata_list:
    histogram[kata] = histogram.get(kata, 0) + 1  

# Cetak hasil histogram
print("Histogram kata:", histogram)
