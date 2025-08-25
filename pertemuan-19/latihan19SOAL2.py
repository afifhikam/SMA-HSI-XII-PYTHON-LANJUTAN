import re

no_telp = input("masukin aja no lu bro: ")
pola = r'^\d+$'
match = re.search(pola, no_telp)

if match:
    if 10 <= len(no_telp) <= 13:
        print("nih no lu ada dan valid broe")
        print(f"panjang no telp lu {len(no_telp)} digit")
    else:
        print("nah ini, no telp lu gak valid bro")
        print(f"panjang no telp lu {len(no_telp)} digit")
else:
    print("format yang lu masukin salah, masukin no telpon aja bre!!")
