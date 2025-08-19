# Dictionary dengan tuple sebagai key

papan_catur = {}

papan_catur[(1, 'a')] = "Benteng Putih"
papan_catur[(1, 'b')] = "Kuda Putih"
papan_catur[(1, 'c')] = "Gajah Putih"
papan_catur[(8, 'h')] = "Benteng Hitam"
papan_catur[(8, 'g')] = "Kuda Hitam"

print("Bidak di (1, 'a'):", papan_catur[(1, 'a')])

print("\nIsi dictionary papan_catur:")
for posisi, bidak in papan_catur.items():
    print(posisi, ":", bidak)
