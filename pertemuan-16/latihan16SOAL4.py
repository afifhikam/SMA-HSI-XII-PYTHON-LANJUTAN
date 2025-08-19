# Buka file

fname = "mbox-short.txt"
fhand = open(fname)

hari_count = {}

for line in fhand:
    
    if line.startswith("From "):
        words = line.split()
        hari = words[2]  
        
        hari_count[hari] = hari_count.get(hari, 0) + 1


print(hari_count)
