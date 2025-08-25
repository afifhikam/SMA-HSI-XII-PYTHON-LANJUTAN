#SOAL 1

import re

data = "Pendapatan bulan ini adalah Rp 1,500,000, sedangkan pengeluaran sebesar Rp 850,000."

pattern = r"\d+"

hasil = re.findall(pattern, data)

print(hasil)

