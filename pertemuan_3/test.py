print("=== Sistem Cek Belanja & Status Pembayaran ===")

nama_pembeli = input("Masukkan nama pembeli: ")
harga_barang = float(input("Harga satuan barang (Rp): "))
jumlah_beli = int(input("Jumlah barang yang dibeli: "))
uang_dibayar = int(input("Uang yang diberikan ke kasir (Rp): ")) #

total_harga = harga_barang * jumlah_beli #
selisih_uang = uang_dibayar - total_harga

uang_cukup = uang_dibayar >= total_harga
uang_pas = uang_dibayar == total_harga
uang_kurang = uang_dibayar < total_harga

print("\n=== Ringkasan Transaksi ===")
print("Nama Pelanggan:", nama_pembeli)
print("Total Harga: Rp", total_harga) #
print("Selisih Uang (Kembalian/Kekurangan): Rp", selisih_uang)

print("\n=== Status Cek Sistem (True/False) ===")
print("Apakah uang yang dibayarkan cukup?  :", uang_cukup)
print("Apakah pembeli membayar uang pas?   :", uang_pas)
print("Apakah pembeli berhutang?           :", uang_kurang)