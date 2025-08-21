# Membuat class Kucing
class Kucing:
    # Constructor dengan parameter nama dan warna
    def __init__(self, nama, warna):
        self.nama = nama
        self.warna = warna

    # Method untuk bersuara
    def bersuara(self):
        print("Meow!")

    # Method untuk memperkenalkan diri
    def perkenalkan_diri(self):
        print(f"Halo, saya kucing bernama {self.nama} dan warna saya {self.warna}.")

# Membuat 2 object (instance) dari class Kucing
kucing1 = Kucing("Oren", "Oranye")
kucing2 = Kucing("Milo", "Coklat")

# Memanggil method pada objek pertama
kucing1.perkenalkan_diri()
kucing1.bersuara()

# Memanggil method pada objek kedua
kucing2.perkenalkan_diri()
kucing2.bersuara()


#  Latihan 1: Class 
# Kucing
#  . Buatlah sebuah 
# class
#  bernama 
# Kucing
#  .
#  . Buat constructor 
# __init__()
#  yang menerima dua parameter: 
# nama
#  dan 
# warna
#  . Constructor ini
#  harus menyimpan nilai-nilai tersebut ke dalam atribut 
# self.nama
#  dan 
# self.warna
#  .
# . Buat sebuah method bernama 
# bersuara()
#  yang tidak memiliki parameter (selain 
# self
#  ). Ketika
#  dipanggil, method ini harus mencetak 
# "Meow!"
#  .
#  . Buat sebuah method bernama 
# perkenalkan_diri()
#  yang mencetak kalimat seperti 
# "Halo, saya
#  kucing bernama [nama] dan warna saya [warna]."
#  .
#  . Buat dua object (instance) dari class 
# Kucing
#  dengan nama dan warna yang berbeda (misal, "Oren"
#  berwarna "Oranye" dan "Milo" berwarna "Coklat").
#  . Panggil method 
# perkenalkan_diri()
#  dan 
# bersuara()
#  dari kedua objek tersebut