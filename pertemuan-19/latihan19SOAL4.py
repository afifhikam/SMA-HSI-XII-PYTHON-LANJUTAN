import re
kalimat = "Kucing, anjing, dan burung adalah hewan peliharaan."
pola = re.findall(r'\w+g\b', kalimat)
print(pola)