class RekeningBank:

    def __init__(self, nomor_rekening, nama_pemilik):
        self.nomor_rekening = nomor_rekening
        self.nama_pemilik = nama_pemilik
        self.saldo = 0  

    def lihat_saldo(self):
        print(f"Saldo {self.nama_pemilik} saat ini: Rp{self.saldo}")

    def setor(self, jumlah):
        self.saldo += jumlah
        print(f"Setor sebesar Rp{jumlah} berhasil. Saldo sekarang: Rp{self.saldo}")

    def tarik(self, jumlah):
        if jumlah > self.saldo:
            print("Saldo tidak mencukupi")
        else:
            self.saldo -= jumlah
            print(f"Tarik sebesar Rp{jumlah} berhasil. Saldo sekarang: Rp{self.saldo}")

# Membuat objek rekening_budi
rekening_budi = RekeningBank("123456789", "Budi")

# Uji coba method
rekening_budi.lihat_saldo()     # cek saldo awal
rekening_budi.setor(500000)     # setor pertama
rekening_budi.setor(200000)     # setor kedua
rekening_budi.tarik(100000)     # tarik uang
rekening_budi.tarik(700000)     # tarik lebih besar dari saldo (gagal)
rekening_budi.lihat_saldo()     # cek saldo akhir
