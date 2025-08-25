import re
teks = "python adalah bahasa terbaik di dalam python, dan python mudah untuk di pelajari."
match = re.search('python', teks)
match1 = re.findall('python', teks)  # UNTUK MENCARI KATA PYTHON KESELURUHAN YANG ADA PADA TEKS TERSEBUT

print(f"hasil 'search': {match.group()}")
print(f"hasil 'findall': {match1}")